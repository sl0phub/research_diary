+++
title = "Breakdown — Threats to Kubernetes: A Layered Approach"
date = 2026-09-17T06:00:00Z
type = "deep-dives"
tags = ["breakdown", "cloud", "vulnerability-discovery", "tooling"]
slug = "kubernetes-threat-breakdown"
summary = "A layered analysis of threats to Kubernetes environments, exploring container escapes, control plane vulnerabilities, and real-world case studies."
+++

## Background

Kubernetes has become the de facto standard for container orchestration, powering the computing continuum from edge devices to massive cloud-native deployments [1]. By design, it provides an expansive API interface and declarative state management, orchestrating complex microservice architectures [2]. However, this complexity introduces a profound shift in the threat model compared to traditional monolithic applications or simple virtual machine (VM) deployments. While containerization offers lightweight resource isolation [17], it shares the underlying host kernel, fundamentally differentiating it from hardware-assisted virtualization and introducing new vectors for privilege escalation and side-channel attacks [3].

The evolution of Kubernetes security has been reactionary. Initially, the platform focused on operational velocity rather than robust isolation, often defaulting to open permissions and anonymous API access [4]. High-profile breaches, such as the Tesla cryptojacking incident [4], highlighted the dangers of exposed, unauthenticated dashboards. In response, the community introduced mechanisms like Role-Based Access Control (RBAC), Pod Security Policies (later replaced by Pod Security Standards), and network policies to harden clusters [4]. Yet, the configuration of these mechanisms remains non-trivial. The sheer number of parameters, default settings, and interactions between components often leads to severe misconfigurations [5].

Moreover, modern cloud-native environments present a fundamentally different exfiltration and lateral movement landscape. Attackers no longer focus solely on dropping payloads onto disk; instead, they target Kubernetes secrets, IAM role tokens, and Terraform state files to pivot across trust boundaries [6]. The integration of Kubernetes into multi-tenant environments, such as cloud providers and scientific computing platforms [7], further complicates the threat landscape, as malicious tenants actively attempt to break isolation to access co-located workloads.


The architectural design of Kubernetes separates concerns between the control plane and the data plane (compute nodes). The control plane is composed of the kube-apiserver, kube-scheduler, kube-controller-manager, and the etcd key-value store. The kube-apiserver acts as the front end for the Kubernetes control plane, exposing a RESTful API that handles all internal and external requests. Every component, from the scheduler making placement decisions to the kubelet reporting node status, communicates through this central hub. This design centralizes state management in etcd, meaning that any entity with direct read or write access to etcd can bypass the API server's authentication and authorization checks entirely, fundamentally breaking the cluster's security model.

On the data plane, the kubelet agent runs on every node, taking instructions from the API server and managing the container runtime (e.g., containerd, CRI-O) to ensure that the pods defined in the specifications are running and healthy. The kube-proxy maintains network rules on nodes, allowing network communication to pods from network sessions inside or outside the cluster. The container runtime itself relies on Linux kernel features—specifically namespaces (Mount, PID, Network, IPC, UTS, and User) to provide isolation, and control groups (cgroups v1/v2) to enforce resource limits on CPU, memory, and I/O. However, because containers do not emulate hardware, they share the host's kernel. A vulnerability in the kernel's network stack, file system drivers, or system call interfaces can be exploited by a malicious container to compromise the host operating system. This shared-kernel architecture is the primary differentiator between container security and traditional virtual machine security, where a hypervisor provides a distinct hardware boundary.

The shift towards microservices running in containers has also introduced service meshes (like Istio or Linkerd) and Container Network Interfaces (CNI) plugins (like Calico, Cilium, or Flannel). These components manage pod-to-pod communication, introducing their own attack surfaces. For example, malicious actors can exploit misconfigured CNI routing tables to intercept traffic (Man-in-the-Middle) or bypass network policies meant to restrict lateral movement.

## Current State

The current state of Kubernetes security can be understood through a layered threat model, progressing from the supply chain down to the infrastructure. The MITRE ATT&CK framework for containers [8] and the OWASP Kubernetes Top Ten [9] categorize these threats based on attacker tactics and techniques. We classify the threats across five primary layers: Supply Chain, Infrastructure, Control Plane, Compute/Worker Nodes, and Pod/Container [10].

### The Container and Pod Layer

The fundamental unit of execution in Kubernetes is the Pod, which encapsulates one or more containers. Containers rely on Linux namespaces (for isolation) and cgroups (for resource limitation) [11]. The primary threat at this layer is the container escape, where an attacker breaks out of the namespace isolation to achieve root execution on the host node.

Container escapes typically manifest through kernel vulnerabilities or misconfigurations. For example, "Container Confusion" vulnerabilities arise when the Linux kernel incorrectly downcasts structure embeddings, leading to type confusion and memory corruption that attackers exploit to overwrite credentials [3]. Another vector involves abusing privileged capabilities. Containers running with `CAP_SYS_ADMIN` or the `privileged` flag can directly manipulate host namespaces or mount the host filesystem, neutralizing any isolation [12].

Recent research has highlighted novel escape mechanisms utilizing the extended Berkeley Packet Filter (eBPF) [13]. While eBPF is heavily adopted for observability and security (e.g., Cilium), malicious eBPF programs loaded from a compromised, privileged container can intercept system calls, steal sensitive data from other containers, and even hijack process execution by altering system call arguments [13]. This "Bewildered eBPF" attack demonstrates that tools designed for security can become powerful weapons if host-level execution contexts are breached.

To combat these threats, practitioners employ alternative runtimes. MicroVM-based containers, such as Kata Containers and Firecracker, provide hardware-assisted isolation, running each pod in a lightweight VM [14]. However, even these environments are not immune. Operation forwarding attacks can break the isolation of microVM-based containers by exploiting the host kernel functions and system calls that handle the microVM's I/O operations [14]. Similarly, WebAssembly (Wasm) is emerging as a secure container alternative due to its linear memory and type checking [15], but attackers can still exploit the WASI/WASIX interfaces to exhaust host resources and interfere with co-located instances [15].

| Defense Mechanism | Mechanism Type | Strengths | Limitations |
|---|---|---|---|
| Seccomp | Syscall Filtering | Reduces the kernel attack surface significantly [16]. | Hard to configure automatically without breaking applications [17]. |
| AppArmor / SELinux | Mandatory Access Control | Prevents arbitrary host mounts and limits file access [18]. | Requires deep OS integration; often disabled due to complexity [19]. |
| MicroVMs (Kata) | Hardware Virtualization | Strong isolation boundaries; mitigates shared kernel exploits [14]. | Operation forwarding vulnerabilities and performance overhead [14]. |
| Wasm Runtimes | Software Fault Isolation | Memory-safe execution environment [15]. | Emerging attack surface via WASI resource exhaustion [15]. |

### The Compute and Worker Node Layer

Worker nodes host the container runtime (e.g., containerd, CRI-O) and the Kubelet. The Kubelet is the primary node agent, responsible for ensuring containers are running in a Pod [20]. Compromising a worker node grants an attacker control over all pods scheduled on that node and access to the Kubelet's credentials, which can often be used to pivot into the control plane [21].

A critical threat at this layer is the exposure of the Kubelet API. If an attacker gains access to an unauthenticated Kubelet API (typically on port 10250), they can execute arbitrary commands (`/exec`) within any pod on the node, effectively bypassing all container-level isolation [22]. Furthermore, attackers can exploit host-path mounts. If a pod is permitted to mount the host's `/var/run/docker.sock` or `/run/containerd/containerd.sock`, the container can communicate directly with the daemon to spawn new, fully privileged containers on the host [23].

Case studies of node-level compromises frequently involve cryptojacking. The TeamTNT group's Hildegard malware specifically targeted Kubernetes environments, leveraging unsecured Kubelets for initial access [24]. Once inside, it used `LD_PRELOAD` to hide its processes and deployed cryptominers across the node's resources. Another example is the Siloscape malware, which targeted Windows containers to escape to the underlying Kubernetes node, opening a backdoor that could facilitate ransomware deployment or supply chain poisoning [25].

### The Control Plane Layer

The control plane is the brain of the Kubernetes cluster, comprising the API Server, etcd, Scheduler, and Controller Manager [26]. The API Server is the central management entity and the primary target for attackers. Access to the API Server is governed by authentication, authorization (primarily RBAC), and admission controllers [27].

Excessive RBAC permissions represent a pervasive misconfiguration in Kubernetes [28]. Over-privileged service accounts mounted into pods allow attackers who compromise a single container to escalate their privileges. For instance, granting a service account the ability to create pods allows an attacker to schedule a privileged pod, escaping to the node [29]. Similarly, the ability to read Secrets (`get/list/watch secrets`) exposes all sensitive credentials stored in the namespace, including database passwords and API tokens [30]. Research on automated capability inference has shown that exposed cloud services frequently suffer from over-privilege, where unprivileged capabilities, when combined, create severe security risks [31].

Mitigating control plane threats requires a strict implementation of the principle of least privilege. However, configuring granular RBAC rules is error-prone. Tools like EPScan have been proposed to automatically detect excessive RBAC permissions [28]. Furthermore, securing API requests requires extending access control beyond standard RBAC. Novel approaches suggest stateful least privilege authorization, allowing client applications to dynamically attenuate the privileges of their tokens, reducing the blast radius of stolen credentials [32]. Additionally, KubeFence proposes fine-grained API filtering tailored to specific client workloads, analyzing operator configurations to restrict unnecessary features of the Kubernetes API [33].

| RBAC Permission | Intended Use | Exploitation Impact |
|---|---|---|
| `create pods` | Deploying workloads | Attacker creates a privileged pod to mount host filesystem and gain root [29]. |
| `list secrets` | Application configuration | Attacker dumps all secrets in the namespace, stealing database credentials [30]. |
| `bind roles` | Managing access control | Attacker grants themselves `cluster-admin` privileges [34]. |
| `create certificates` | Managing TLS | Attacker generates a valid certificate for a control plane component to bypass auth [35]. |

### The Infrastructure and Cloud Layer

Kubernetes rarely operates in a vacuum; it is deeply integrated with the underlying cloud provider's infrastructure (AWS, GCP, Azure). This integration introduces the Cloud Metadata API as a critical threat vector [36].

If a pod is compromised, an attacker can query the metadata service (e.g., `169.254.169.254`) to retrieve the temporary IAM credentials assigned to the worker node [37]. With these credentials, the attacker can pivot out of the Kubernetes cluster and attack the broader cloud environment, potentially accessing S3 buckets, modifying routing tables, or launching new instances [38].

The "Capital One" breach exemplifies the severity of this vector. Although not strictly Kubernetes, the attack involved exploiting a misconfigured firewall (acting similarly to a compromised workload) to access the metadata service and steal credentials, ultimately leading to massive data exfiltration [39]. In Kubernetes, preventing metadata abuse requires configuring network policies to block pod egress to the metadata IP, or utilizing features like AWS IAM Roles for Service Accounts (IRSA) or GKE Workload Identity, which map Kubernetes service accounts directly to IAM roles, eliminating the need to expose node-level credentials [40].

Attribution in cloud-native environments also poses unique challenges. The ephemeral nature of pods means the infrastructure that initiated an attack may no longer exist during the forensic investigation [41]. The CLOUDBURST framework highlights that infrastructure ephemerality and complex IAM role assumption chains require new methodologies for post-exfiltration attribution, utilizing passive beacons and explicit temporal modeling [41].


### Network and Communications Layer

The network layer within a Kubernetes cluster presents unique challenges due to its highly dynamic nature. Pods are ephemeral, constantly being created and destroyed, leading to rapidly changing IP addresses. Kubernetes uses the CNI to manage these virtual networks, and the kube-proxy to load-balance traffic across services using iptables, IPVS, or eBPF.

A primary threat at the network layer is lateral movement. By default, Kubernetes implements a "flat network" model where any pod can communicate with any other pod across all namespaces, unless explicitly restricted by NetworkPolicies. If an attacker compromises a frontend web server pod, they can typically route traffic directly to the backend database pods or internal caching layers without restriction.

Moreover, the complexity of overlay networks introduces vulnerabilities in the CNI plugins themselves. For instance, attacks targeting the Encapsulation protocols (like VXLAN or Geneve) can manipulate packet headers to spoof origins or bypass firewall rules. If the cluster lacks encryption for pod-to-pod traffic (such as WireGuard or IPsec implemented via the CNI), attackers who have gained access to the underlying node network can sniff sensitive plaintext data traversing the cluster.

To mitigate these threats, organizations implement default-deny NetworkPolicies and deploy service meshes to enforce mutual TLS (mTLS) for all inter-service communication. mTLS ensures that traffic is both encrypted in transit and cryptographically authenticated, preventing a compromised pod from impersonating another service. However, deploying a service mesh introduces sidecar proxy containers (like Envoy) into every pod, which themselves can suffer from vulnerabilities (e.g., HTTP/2 rapid reset attacks) that lead to resource exhaustion and denial of service.

| Network Defense | Mitigation Strategy | Technical Cost |
|---|---|---|
| Default-Deny NetworkPolicy | Drops all ingress/egress traffic not explicitly allowed | High operational overhead to map all valid communication paths |
| Service Mesh mTLS | Cryptographic identity and encryption in transit | Increases latency and CPU overhead due to sidecar proxies and TLS handshakes |
| CNI Encryption (WireGuard) | Node-to-node traffic encryption | Limits visibility for traditional network intrusion detection systems |
| Egress Gateways | Funnels all external traffic through dedicated, monitored nodes | Creates a potential network bottleneck and single point of failure |

### Data Storage and Volume Layer

Kubernetes manages persistent data through PersistentVolumes (PV) and PersistentVolumeClaims (PVC). These volumes can be backed by local host storage, network-attached storage (NFS, iSCSI), or cloud provider block storage (AWS EBS, GCP PD). The security of this data at rest and in transit is a critical concern.

A significant threat at the storage layer is the unauthorized mounting of sensitive volumes. If an attacker compromises a pod that has access to a shared NFS volume, they might be able to read or modify data belonging to other tenants. Furthermore, hostPath volumes are notoriously dangerous; they allow a pod to mount any directory from the host node's filesystem. An attacker mapping `/` or `/var/log` from the host can easily read sensitive node configuration files, extract kubelet credentials, or tamper with the container runtime binaries.

Encryption at rest is paramount for mitigating data exposure if the underlying storage medium is compromised. While cloud providers often encrypt block storage by default, Kubernetes also offers the ability to encrypt Secrets directly in the etcd database. Without this feature enabled (via the `EncryptionConfiguration` resource), Secrets are stored in plaintext (merely base64 encoded) within etcd. If an attacker gains read access to the etcd data store—either through a misconfigured API server, a compromised etcd node, or a backup file—they instantly obtain all the cluster's sensitive credentials.

The Container Storage Interface (CSI) drivers, which integrate third-party storage systems into Kubernetes, also expand the attack surface. Vulnerabilities in CSI drivers running as privileged DaemonSets on worker nodes can be exploited to achieve privilege escalation or node compromise. Defending this layer requires strict admission control policies (e.g., OPA Gatekeeper) to outright reject pods attempting to use hostPath mounts, coupled with robust RBAC to limit who can create or attach PersistentVolumes.

### The Supply Chain Layer

The supply chain represents the earliest phase of the threat lifecycle. Attackers target the images deployed into the cluster and the CI/CD pipelines that build them [42].

Malicious container images are routinely uploaded to public registries like Docker Hub [43]. These images often masquerade as legitimate software but contain embedded cryptominers, backdoors, or exploit code. If a Kubernetes manifest references a compromised image, the cluster will unknowingly pull and execute the malicious payload [17].

Furthermore, vulnerabilities in the software dependencies packaged within the images (e.g., outdated libraries) provide initial access vectors. Log4Shell demonstrated how a single vulnerability in a ubiquitous logging library could compromise thousands of containerized Java applications worldwide [18]. Java web containers are also susceptible to Data Retention Denial-of-Service (DRDoS) vulnerabilities, where careless data management allows attackers to exhaust memory resources through specially crafted requests [44].

Defending the supply chain requires image scanning (e.g., Trivy, Clair) to detect known CVEs before deployment [19]. However, empirical evaluations of static configuration scanners reveal significant disparities in coverage and detection accuracy, highlighting the need for standardized risk assessment approaches [10]. Additionally, image signing (e.g., Sigstore/Cosign) and admission controllers (e.g., OPA Gatekeeper, Kyverno) can enforce policies ensuring only signed, vetted images from trusted registries are allowed into the cluster [11].

## Future Outlook

The trajectory of Kubernetes security points toward continuous runtime enforcement and AI-driven remediation, though significant challenges remain regarding context awareness and topology dependencies.

Large Language Models (LLMs) are being explored to automate cluster security remediation, generating configuration patches from Kubernetes Security Posture Management (KSPM) findings [45]. However, generating these patches in isolation often breaks live service dependencies. The KuTIE system demonstrates that providing LLMs with runtime topology context (e.g., Istio call edges and service account bindings) significantly improves the correctness of generated patches, bridging the gap between static compliance and functional stability [46].

Confidential computing is also emerging as a critical frontier for securing multi-tenant clusters. Hardware features like AMD SEV and Intel TDX provide memory encryption, ensuring that even a compromised host cannot read the memory of guest VMs [47]. For serverless functions running on Kubernetes, split container designs propose creating confidential virtual machines with a minimal trusted computing base, deploying a function-oriented OS within the CVM while delegating management to the untrusted host [48].

However, attackers will adapt. As defenses against memory corruption mature, we anticipate a rise in architectural and logic flaws. Semi-automated threat modeling approaches, which combine static configuration analysis with observed network flows to construct runtime architecture graphs, will become necessary to detect multi-stage attacks that chain vulnerabilities across trust boundaries [49].


## References

1. Rossi, B. et al. "Comparative Analysis of Lightweight Kubernetes Distributions for Edge Computing: Security, Resilience and Maintainability." arXiv 2025. http://arxiv.org/abs/2503.04815v1
2. N. K. et al.. "The Kubernetes Security Landscape: AI-Driven Insights from Developer Discussions." 2020. http://arxiv.org/abs/2409.04647v1
3. Koschel, J. et al. "Uncontained: Uncovering Container Confusion in the Linux Kernel." USENIX Security 2023. https://www.usenix.org/system/files/usenixsecurity23-koschel.pdf
4. M. E. R. et al. "XI Commandments of Kubernetes Security: A Systematization of Knowledge Related to Kubernetes Security Practices." arXiv 2020. http://arxiv.org/abs/2006.15275v1
5. Y. S. et al. "Centralized Defense: Logging and Mitigation of Kubernetes Misconfigurations with Open Source Tools." arXiv 2024. http://arxiv.org/abs/2408.03714v1
6. J. H. et al. "Network and Device Level Cyber Deception for Contested Environments Using RL and LLMs." IEEE S&P 2025. http://arxiv.org/abs/2603.17272v2
7. J. M. et al. "The National Research Platform: Stretched, Multi-Tenant, Scientific Kubernetes Cluster." arXiv 2025. http://arxiv.org/abs/2505.22864v1
8. MITRE. "Matrix - Enterprise - Containers | MITRE ATT&CK." 2021. https://attack.mitre.org/matrices/enterprise/containers/
9. OWASP. "OWASP Kubernetes Top Ten." 2022. https://owasp.org/www-project-kubernetes-top-ten/
10. M. K. et al. "A Comparison of Kubernetes Compliance Standards and Configuration Scanners." arXiv 2026. http://arxiv.org/abs/2606.24438v1
11. S. H. et al. "Toward Smart Moving Target Defense for Linux Container Resiliency." arXiv 2016. http://arxiv.org/abs/1611.03065v2
12. B. G. et al. "Making Secure Software Insecure without Changing Its Code: The Possibilities and Impacts of Attacks on the DevOps Pipeline." arXiv 2022. http://arxiv.org/abs/2201.12879v1
13. Y. He, R. Guo, Y. Xing, X. Che, K. Sun, Z. Liu, K. Xu, and Q. Li. "Cross Container Attacks: The Bewildered eBPF on Clouds." USENIX Security 2023. https://www.usenix.org/system/files/usenixsecurity23-he.pdf
14. J. Xiao, N. Yang, W. Shen, J. Li, X. Guo, Z. Dong, F. Xie, and J. Ma. "Attacks are Forwarded: Breaking the Isolation of MicroVM-based Containers Through Operation Forwarding." USENIX Security 2023. https://www.usenix.org/system/files/usenixsecurity23-xiao-jietao.pdf
15. Z. Yu, D. Zhan, L. Ye, H. Yu, H. Zhang, and Z. Tian. "Exploring and Exploiting the Resource Isolation Attack Surface of WebAssembly Containers." USENIX Security 2025. https://www.usenix.org/system/files/usenixsecurity25-yu-zhaofeng.pdf
16. G. M. et al. "A Stone-Cech Collecting Semantics for Residual Process Behaviour." arXiv 2026. http://arxiv.org/abs/2606.17228v1
17. L. S. et al. "Escape the Fake: Introducing Simulated Container-Escapes for Honeypots." arXiv 2021. http://arxiv.org/abs/2104.03651v1
18. M. P. et al. "Resource-Interaction Graph: Efficient Graph Representation for Anomaly Detection." arXiv 2022. http://arxiv.org/abs/2212.08525v1
19. R. B. et al. "LLMSecConfig: An LLM-Based Approach for Fixing Software Container Misconfigurations." arXiv 2025. http://arxiv.org/abs/2502.02009v1
20. Kubernetes Documentation. "Kubelet." kubernetes.io 2024. https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/
21. H. S. et al. "SQUIRO: A Framework for Security-Aware Quantum-Classical Scheduling on Kubernetes." arXiv 2026. http://arxiv.org/abs/2607.16089v1
22. C. L. et al. "Implementation of New Security Features in CMSWEB Kubernetes Cluster at CERN." arXiv 2024. http://arxiv.org/abs/2405.15342v1
23. D. F. et al. "Comparing Security and Efficiency of WebAssembly and Linux Containers in Kubernetes." arXiv 2024. http://arxiv.org/abs/2411.03344v1
24. Sasson, A. et al. "Hildegard: New TeamTNT Cryptojacking Malware Targeting Kubernetes." Palo Alto Networks Unit 42 2021. https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/
25. Prizmant, D. "Siloscape: First Known Malware Targeting Windows Containers to Compromise Cloud Environments." Palo Alto Networks Unit 42 2021. https://unit42.paloaltonetworks.com/siloscape/
26. Kubernetes Documentation. "Kubernetes Components." kubernetes.io 2024. https://kubernetes.io/docs/concepts/overview/components/
27. A. A. et al. "Inside Job: Defending Kubernetes Clusters Against Network Misconfigurations." arXiv 2025. http://arxiv.org/abs/2506.21134v1
28. W. K. et al. "Structured but Fragile: On the Limits of LLMs in Cybersecurity Decision-Making." IEEE S&P 2025. http://arxiv.org/abs/2608.20966v1
29. Z. W. et al. "Breaking the Bulkhead: Demystifying Cross-Namespace Reference Vulnerabilities in Kubernetes Operators." arXiv 2025. http://arxiv.org/abs/2507.03387v3
30. Gunathilake, K. et al. "K8s Pro Sentinel: Extend Secret Security in Kubernetes Cluster." arXiv 2024. http://arxiv.org/abs/2411.16639v1
31. Wang, X. et al. "Credit Karma: Understanding Security Implications of Exposed Cloud Services through Automated Capability Inference." USENIX Security 2023. https://www.usenix.org/system/files/usenixsecurity23-wang-xueqiang-karma.pdf
32. Cao, L. et al. "Stateful Least Privilege Authorization for the Cloud." USENIX Security 2024. https://www.usenix.org/system/files/usenixsecurity24-cao-leo.pdf
33. T. M. et al. "KubeFence: Security Hardening of the Kubernetes Attack Surface." arXiv 2025. http://arxiv.org/abs/2504.11126v1
34. J. L. et al. "Agent Name Service (ANS): A Proof-of-Concept Trust Layer for Secure AI Agent Discovery." arXiv 2026. http://arxiv.org/abs/2604.26997v1
35. S. M. et al. "Securing the Open RAN Infrastructure: Exploring Vulnerabilities in Kubernetes Deployments." arXiv 2024. http://arxiv.org/abs/2405.01888v1
36. Raffa, G. et al. "CloudFlow: Identifying Security-sensitive Data Flows in Serverless Applications." USENIX Security 2025. https://www.usenix.org/system/files/usenixsecurity25-raffa.pdf
37. M. G. et al. "SPARK: Secure Predictive Autoscaling for Robust Kubernetes." arXiv 2026. http://arxiv.org/abs/2603.26833v1
38. J. L. et al. "Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare." arXiv 2026. http://arxiv.org/abs/2603.17419v1
39. M. A. et al. "A Big Data Architecture for Early Identification and Categorization of Dark Web Sites." arXiv 2024. http://arxiv.org/abs/2401.13320v1
40. S. P. et al. "AAGATE: A NIST AI RMF-Aligned Governance Platform for Agentic AI." arXiv 2025. http://arxiv.org/abs/2510.25863v2
41. A. R. et al. "CLOUDBURST: Cloud-Layer Observations Using Beacons for Unified Real-time Surveillance and Threat Attribution." arXiv 2026. http://arxiv.org/abs/2605.12976v1
42. P. S. et al. "Enhancing Software Supply Chain Security Through STRIDE-Based Threat Modelling of CI/CD Pipelines." arXiv 2025. http://arxiv.org/abs/2506.06478v1
43. R. B. et al. "Exploiting and Securing Docker containers and Kubernetes pods from a MitM attack." arXiv 2026. http://arxiv.org/abs/2609.16253v1
44. Lian, K. et al. "Careless Retention and Management: Understanding and Detecting Data Retention Denial-of-Service Vulnerabilities in Java Web Containers." USENIX Security 2025. https://www.usenix.org/system/files/usenixsecurity25-lian.pdf
45. M. H. et al. "CTI-REALM: Benchmark to Evaluate Agent Performance on Security Detection Rule Generation Capabilities." arXiv 2026. http://arxiv.org/abs/2603.13517v2
46. D. T. et al. "Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?" arXiv 2026. http://arxiv.org/abs/2607.25995v2
47. Shi, J. et al. "Serverless Functions Made Confidential and Efficient with Split Containers." USENIX Security 2025. https://www.usenix.org/system/files/usenixsecurity25-shi-jiacheng.pdf
48. F. W. et al. "C8s: A Confidential Kubernetes Architecture." arXiv 2026. http://arxiv.org/abs/2604.26974v1
49. S. M. et al. "Semi-Automated Threat Modeling of Cloud-Based Systems Through Extracting Software Architecture from Configuration and Network Flow." arXiv 2026. http://arxiv.org/abs/2603.22603v1
