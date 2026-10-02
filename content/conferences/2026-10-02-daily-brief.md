+++
title = "Conference Brief — 2026-10-02"
date = 2026-10-02T06:00:00Z
type = "conferences"
tags = ["fuzzing", "browser", "vulnerability-discovery", "web-security", "hardware", "ndss"]
summary = "New approaches to uncovering complex state bugs in JavaScript engines, DOM-XSS via user interactions, hidden IoT interfaces, and electromagnetic fault injection on Hall-effect keyboards."
+++

## In brief

- Fuzzing advances move beyond passive discovery by instrumenting the engine for fine-grained differential state extraction and combining dynamic symbolic execution with interaction synthesis.
- Hardware and firmware attack surfaces expand as researchers successfully inject faults into Hall-effect keyboards and systematically uncover undocumented, privileged interfaces in IoT devices.

## DUMPLING: Fine-grained Differential JavaScript Engine Fuzzing

- A new differential fuzzer that compares interpreted and optimized JIT compiled execution by instrumenting the JavaScript engine itself, allowing introspection in the middle of JIT compiled functions.
- Previous differential fuzzing techniques relied on inserting JS functions to read states, which hindered JIT optimization and struggled to discover subtle bugs where miscalculations happen before memory corruption.
- DUMPLING found eight new bugs in the V8 engine, demonstrating the effectiveness of high-frequency fine-grained execution state extraction.

Wachter, L. et al. "DUMPLING: Fine-grained Differential JavaScript Engine Fuzzing." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/dumpling-fine-grained-differential-javascript-engine-fuzzing/

## DOM-XSS Detection via Webpage Interaction Fuzzing and URL Component Synthesis

- Prior automated detection for DOM-XSS missed vulnerabilities requiring user interaction to execute event handlers and lacked discovery of code paths unlocked by specific URL components like GET parameters.
- SWIPE combines user interaction fuzzing with dynamic symbolic execution to synthesize URL parameters and fragments, actively exploring previously unreached event-driven code paths.
- Running SWIPE on 44,480 URLs found 15% more vulnerabilities than prior tools and 20 new vulnerabilities unlocked directly by the synthesized URL parameters and fragments.

Sabino, N. et al. "DOM-XSS Detection via Webpage Interaction Fuzzing and URL Component Synthesis." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/dom-xss-detection-via-webpage-interaction-fuzzing-and-url-component-synthesis/

## EAGLEYE: Exposing Hidden Web Interfaces in IoT Devices via Routing Analysis

- Hidden web interfaces in IoT firmware introduce severe risks but evade traditional bug detection because they lack obvious static patterns or fuzzing feedback.
- EAGLEYE analyzes public interface requests to extract routing tokens (e.g., action names) and uses LLMs to deduce the pattern, building a high-quality dictionary for directed black-box fuzzing.
- The tool discovered 79 hidden interfaces across 13 commercial IoT devices—yielding 29 unknown vulnerabilities like command injection and backdoors.

Liu, H. et al. "EAGLEYE: Exposing Hidden Web Interfaces in IoT Devices via Routing Analysis." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/eagleye-exposing-hidden-web-interfaces-in-iot-devices-via-routing-analysis/

## DualStrike: Accurate, Real-time Eavesdropping and Injection of Keystrokes on Commodity Keyboards

- DualStrike demonstrates the first non-invasive remote attack capable of both keystroke eavesdropping and per-key injection targeting commodity Hall-effect keyboards.
- The attack leverages a custom electromagnet design for high-frequency magnetic spoofing and a magnetometer-based listening mechanism to compromise the magnetic continuous-motion sensors without hardware modifications.
- The attack achieves over 98.9% injection accuracy across six models and can maintain 98.5% accuracy even with a 4 cm displacement offset.

Chen, X. et al. "DualStrike: Accurate, Real-time Eavesdropping and Injection of Keystrokes on Commodity Keyboards." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/dualstrike-accurate-real-time-eavesdropping-and-injection-of-keystrokes-on-commodity-keyboards/
