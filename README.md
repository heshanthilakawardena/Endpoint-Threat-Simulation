# Endpoint Threat Simulation & FIM Engine 🛡️

> **⚠️ STRICT ETHICAL DISCLAIMER:** > This project was developed entirely for educational purposes, academic research, and personal portfolio demonstration. The scripts provided here are designed to simulate endpoint attacks and validate defensive monitoring logic on authorized, local machines *only*. **Do not** deploy or use any part of this code on systems you do not own or do not have explicit, written permission to audit. 

## 📖 Project Overview
This repository contains a local "Red vs. Blue" team simulation designed to demonstrate how endpoint input hooking works and how defenders can catch it in real-time. 

The project is split into two components:
1. **The Attacker (Red Team):** A Python-based keystroke interceptor that uses OS-level API hooking to capture input and save it locally.
2. **The Defender (Blue Team):** A File Integrity Monitoring (FIM) daemon that watches the file system for unauthorized asynchronous I/O operations and throws critical alerts when the attacker script attempts to write data.

## 🛠️ Technologies & Concepts
* **Language:** Python 3.x
* **Libraries:** `pynput` (user-land API hooking), `watchdog` (file system events)
* **Concepts Demonstrated:**
  * Operating System API Hooking (macOS/Windows)
  * File Integrity Monitoring (FIM) & Detection Engineering
  * Endpoint Detection and Response (EDR) basics

