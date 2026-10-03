+++
title = "Breakdown — A Study of Google Jules"
date = 2026-10-03T00:00:00Z
type = "deep-dives"
tags = ["breakdown", "llm-security", "tooling"]
slug = "a-study-of-google-jules"
summary = "A review of Google Jules's agent architecture, capabilities, and vulnerabilities to prompt injection based on public security research and unofficial internals documentation."
+++

## Background

Google Jules is an asynchronous coding agent designed to operate within a development virtual machine. Recent security research by embrace the red and unofficial documentation hosted on an aislopping domain have shed light on the system's architecture, including its toolset, network configurations, and execution boundaries. These sources present a picture of a capable multi-agent system that relies on a primary agent for task planning, delegating execution to worker agents with specialized tools [1] [2].

The unofficial documentation of Jules Internals reveals a robust set of tools categorized into code management, execution and environment, web and media, and user interaction, reflecting a powerful development assistant [3]. However, this extensive capability set, combined with the agent's automated workflows, introduces significant security considerations.

## Current State

Recent security analyses have demonstrated that Google Jules is susceptible to prompt injection attacks, primarily due to its automated tool invocation and execution environment configurations.

### Agent Architecture and Capabilities

The unofficial Jules documentation catalogs the agent's capabilities and environment:

| Category | Tools and Environment |
|---|---|
| Code and File Management | `list_files`, `read_file`, `write_file`, `replace_with_git_merge_diff`, `delete_file`, `rename_file`, `reset_all`, `restore_file` |
| Execution and Environment | `run_in_bash_session`, `start_live_preview_instructions` |
| Web and Media | `google_search`, `view_text_website`, `view_image`, `read_image_file`, `read_media_file` |
| Environment Configuration | Outbound internet access, passwordless sudo, access to various programming toolchains (Python, Node, Java, Go, Rust, etc.) |

Source: Unofficial Jules Internals Documentation [3] [4].

The system prompt indicates that Jules employs a primary agent for planning, while worker agents execute the subtasks. Instructions and contextual information, such as repository-specific `AGENTS.md` guidelines, are injected dynamically into the context [2].

### Prompt Injection and Exploitation

Security research on embracethered.com highlights multiple attack vectors exploiting Jules's architecture. A critical vulnerability stems from the agent's automated workflow, specifically its feature that allows it to process GitHub issues when tagged [5].

The identified attack chains often follow this pattern:
1. **Prompt Injection:** Malicious instructions are embedded in untrusted sources, such as GitHub issues or external websites. In one demonstration, an attacker used invisible Unicode characters (ASCII Smuggler) within a GitHub issue to hide instructions [5].
2. **Confused Deputy / Automatic Tool Invocation:** Jules processes the untrusted input, incorporates the hidden instructions into its plan, and auto-approves the plan (which occurs after a set time delay, observed to be up to 120 seconds) [6].
3. **Execution:** The agent then automatically invokes tools to fulfill the plan.

Specific exploitation scenarios include:
- **Data Exfiltration:** Jules was tricked into using the `view_text_website` tool to visit a malicious URL, appending sensitive information gathered earlier in the chat to the URL, resulting in data exfiltration [1].
- **Remote Code Execution (RCE):** The `run_in_bash_session` tool, combined with unrestricted outbound internet access, allows an attacker to instruct Jules to download and execute malware. A proof-of-concept demonstrated downloading the Sliver C2 framework, turning the Jules instance into a remote-controlled zombie agent ("ZombAI") [6].
- **Code Backdooring:** Hidden instructions in a GitHub issue successfully coerced Jules into adding a backdoor function and executing it within a repository [5].

### Unofficial Internals vs. Standard Security Testing

The unofficial documentation at jules-internals.aislop.ing details execution environments (including Python toolchains and Docker) and configurations (such as passwordless sudo). However, from the perspective of standard sandbox-testing methodologies, the documentation lacks critical details regarding the *boundaries* and *isolation* of these features.

Specific missing details relevant to standard testing include:

*   **Process Isolation Mechanisms:** The documentation confirms Docker is installed but does not specify if the Jules agent process itself runs within a constrained container (e.g., restricted namespaces, dropped capabilities) or directly on the VM host. Testing methodologies require this to understand if process breakout is possible.
*   **Network Ingress and Egress Filtering Rules:** The documentation lacks specifics on firewall rules (like `iptables` or cloud-provider security groups). Standard testing needs to know if internal metadata endpoints (e.g., `169.254.169.254` in cloud environments) are blocked or if inbound connections are possible.
*   **Filesystem Mounts and Read-Only Restrictions:** The agent operates in `/app` and has a home directory `/home/jules`, but it is undocumented whether system directories (`/etc`, `/bin`, `/var/run/docker.sock`) are mounted read-only. Testing relies on this to assess lateral movement or privilege escalation via system files.
*   **Resource Quotas (cgroups):** There is no mention of CPU, memory, or disk I/O limits. Sandbox testing methodologies assess whether a compromised agent can perform resource exhaustion (Denial of Service) attacks against the host environment.
*   **Monitoring and Audit Logging:** The documentation does not detail if agent actions (tool invocations, bash commands) are logged externally to a secure audit trail. Standard security assessments evaluate if an attacker can manipulate or bypass logging to hide their tracks.

These blind spots in the documentation are exactly the areas attackers target to move from "Excessive Agency" to full host compromise.

### Official Documentation vs. External Research

A comparison between the official marketing documentation at `jules.google` and external security research reveals a gap between high-level promises and low-level capabilities.

| Feature Area | Official Documentation | External Research & Internals |
|---|---|---|
| **Capabilities** | "Jules does coding tasks you don't want to do." Highlights Bug Fixing, Version Bump, Tests, and Feature Building [7]. | Exposes a comprehensive toolset including bash execution (`run_in_bash_session`), direct file manipulation, and web access (`view_text_website`, `google_search`) [3]. |
| **Execution Environment** | "Jules fetches your repository, clones it to a Cloud VM, and develops a plan" [7]. | Details reveal passwordless sudo, unrestricted outbound internet access, and pre-installed toolchains [4]. |
| **Workflow** | Describes a human-in-the-loop process: Jules creates a PR, which the user browses and approves [7]. | Demonstrates that Jules auto-approves plans (e.g., within 120 seconds) and automatically executes tool workflows, making it vulnerable to "Confused Deputy" attacks [5] [6]. |
| **Security Boundaries** | Silent on specific sandboxing limits, network egress controls, or isolation mechanisms [7]. | Research shows prompt injections can lead to data exfiltration via URL appending and remote code execution by downloading C2 frameworks [1] [6]. |

The official documentation focuses on user workflow and productivity ("More time for the code you want to write") [7], leaving the extensive capabilities and their associated risks largely undocumented to the end-user. The silence on sandbox isolation mechanisms contrasts with external findings that the VM allows unrestricted outbound network access and shell execution.

### Standard Testing Methodologies for Agent Sandboxes

The vulnerabilities exposed in Google Jules highlight the necessity of rigorous security testing for AI agent sandboxes. Evaluating these environments involves probing for "Excessive Agency" [8] and assessing isolation mechanisms. Standard methodologies focus on several key areas:

*   **Network Egress Monitoring:** Testers check if the agent can initiate arbitrary outbound connections. Unrestricted egress, as seen in Jules, allows data exfiltration and the downloading of malicious payloads [1] [6]. Security researchers typically attempt to fetch external URLs or establish reverse shells to verify network isolation.
*   **Filesystem Integrity and Enumeration:** Evaluations assess whether the agent is confined to a specific workspace. This involves attempting to read sensitive host files (e.g., `/etc/passwd`), enumerate environment variables, or write to directories outside the designated project folder.
*   **Process and Execution Boundaries:** Testers examine the agent's ability to execute shell commands and its privilege level. The presence of passwordless `sudo` or the ability to list and terminate other processes indicates weak isolation.
*   **Proxy-Based Traffic Interception:** Security tools are often deployed to monitor and intercept traffic between the agent and its LLM backend, as well as traffic to external web resources, ensuring that the agent cannot be manipulated into performing server-side request forgery (SSRF) or exfiltrating data via manipulated URLs.

Organizations like OWASP highlight these risks under vulnerabilities such as "LLM06:2025 Excessive Agency", which occurs when an LLM is granted unnecessary functionality, permissions, or autonomy [8]. Furthermore, initiatives like the "Month of AI Bugs" by Embrace The Red actively raise awareness by responsibly disclosing novel vulnerabilities in agentic systems, emphasizing the need for proactive defense and shorter triage windows [9].

### Identified Gaps and Future Documentation Efforts

The discrepancies between the official marketing documentation, the unofficial internals catalog, and the practical findings from security researchers highlight significant gaps in the public data regarding Google Jules.

1.  **Lack of Formal Security Boundary Definitions:** The most glaring gap is the absence of a formally defined security model from Google. Without official documentation on what Jules is *designed* to be restricted from doing, researchers can only infer limitations through trial and error.
2.  **Opacity on Mitigation Mechanisms:** It remains unclear if the auto-approval delay (120 seconds) is intended as a security feature (a window for human intervention) or merely a functional timeout. Public data lacks details on whether there are built-in heuristics to detect anomalous tool usage.

**Targeted Suggestions for Future Internals Documentation:**

To improve the security posture and transparency of agentic systems like Jules, future documentation efforts should explicitly focus on the sandboxing architecture:

*   **Explicitly Document Sandbox Limits:** Internals documentation should move beyond cataloging available tools and explicitly state the restrictions. For example, detailing the exact network egress rules and container isolation policies.
*   **Detail Threat Models:** Documenting the assumed threat model (e.g., "We assume untrusted code in the repository, but trust the GitHub issue text") would clarify the design intent and help focus security research on valid bypasses.
*   **Document Audit Trails:** Future documentation should outline how agent actions are logged and where these logs are stored, providing developers with the tools to audit agent behavior for compromises.

## Future Outlook

The identified vulnerabilities in Google Jules highlight the broader challenges of securing autonomous coding agents. The current mitigation strategies rely heavily on user caution, advising against tasking Jules with untrusted data or providing access to critical private code and secrets [5] [6].

Moving forward, securing such systems will likely require more robust isolation mechanisms, stricter validation of tool inputs, and potentially human-in-the-loop requirements for sensitive actions like code execution or outbound network requests. The tension between agent autonomy and security remains an open problem in the field of LLM-integrated development environments.

## References

1. embrace the red. "Google Jules: Vulnerable to Multiple Data Exfiltration Issues." embracethered.com — https://embracethered.com/blog/posts/2025/google-jules-vulnerable-to-data-exfiltration-issues/
2. Jules Internals. "System Prompts - Jules Internals." jules-internals.aislop.ing — https://jules-internals.aislop.ing/jules-agent/system_prompt/
3. Jules Internals. "Tools - Jules Internals." jules-internals.aislop.ing — https://jules-internals.aislop.ing/jules-agent/tools/
4. Jules Internals. "Environment - Jules Internals." jules-internals.aislop.ing — https://jules-internals.aislop.ing/jules-vm/environment/
5. embrace the red. "Google Jules is Vulnerable To Invisible Prompt Injection." embracethered.com — https://embracethered.com/blog/posts/2025/google-jules-invisible-prompt-injection/
6. embrace the red. "Jules Zombie Agent: From Prompt Injection to Remote Control." embracethered.com — https://embracethered.com/blog/posts/2025/google-jules-remote-code-execution-zombai/
7. Google. "Jules." jules.google — https://jules.google/
8. OWASP. "LLM06:2025 Excessive Agency." genai.owasp.org — https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
9. Embrace The Red. "The Month of AI Bugs." monthofaibugs.com — https://monthofaibugs.com/
