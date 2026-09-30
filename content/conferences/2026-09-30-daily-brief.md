+++
title = "Conference Brief — 2026-09-30"
date = 2026-09-30T06:00:00Z
type = "conferences"
tags = ["cloud", "network-security", "kernel", "ndss"]
summary = "Security analyses of ESXi VMKernel access control, detecting IMSI-catchers through causal messages, and simplifying Data-Oriented Programming in Linux."
+++

## In brief

- This batch covers privilege escalation pathways in the Linux kernel via Data-Oriented Programming and through developer-reserved syscall interfaces in VMware ESXi.
- A standards-driven methodology effectively identified IMSI-catchers in the wild by characterizing specific causal messages rather than relying on correlated behavioral anomalies.

## Demystifying the Access Control Mechanism of ESXi VMKernel

- VMware ESXi uses a proprietary, closed-source mandatory access control mechanism in its VMKernel to enforce privilege isolation and sandbox restrictions.
- By developing a domain-control structure oriented analysis method and a structure-aware debugging framework, researchers reconstructed VMKernel's internal permission logic.
- They uncovered 14 vulnerabilities, including writable in-memory control structures and developer-reserved syscall interfaces, allowing attackers to bypass sandbox restrictions and escalate privileges.

Liu, Y. et al. "Demystifying the Access Control Mechanism of ESXi VMKernel." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/demystifying-the-access-control-mechanism-of-esxi-vmkernel/

## Detecting IMSI-Catchers by Characterizing Identity Exposing Messages in Cellular Traffic

- Prior IMSI-catcher detection tools have focused on correlated behaviors like ephemeral base stations or weak ciphers, leading to high false-positive rates during benign network changes.
- This paper introduces a standards-driven methodology that identifies 53 specific messages an adversary can use to force an IMSI exposure, focusing on causal attributes rather than correlated anomalies.
- By establishing a baseline ratio of these messages through a two-continent measurement study, the approach detected anomalous behavior at a large-scale public event with statistical significance ($p \ll 0.005$).

Tucker, T. et al. "Detecting IMSI-Catchers by Characterizing Identity Exposing Messages in Cellular Traffic." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/detecting-imsi-catchers-by-characterizing-identity-exposing-messages-in-cellular-traffic/

## DirtyFree: Simplified Data-Oriented Programming in the Linux Kernel

- As Kernel Control-Flow Integrity (KCFI) mitigates return-oriented programming (ROP) attacks, Data-Oriented Programming (DOP) has become a primary alternative for privilege escalation.
- Traditional DOP attacks are complex and multistaged, but this paper introduces DIRTYFREE, a systematic method that uses an arbitrary free primitive to force deallocation of attacker-controlled kernel objects.
- The technique successfully exploited 24 real-world kernel vulnerabilities, and the authors also propose two mitigations that prevent exploitation with negligible performance overhead.

Lee, Y. et al. "DirtyFree: Simplified Data-Oriented Programming in the Linux Kernel." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/dirtyfree-simplified-data-oriented-programming-in-the-linux-kernel/
