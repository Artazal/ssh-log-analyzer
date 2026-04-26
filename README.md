# ssh_log_analyzer
CLI tool for analyzing SSH logs and detecting suspicious login attempts.

Simple CLI tool for analyzing SSH logs on Linux servers.

Detects failed login attempts, aggregates them by IP, and highlights suspicious or brute-force activity using data from `journalctl`.

---

## Features

- Count failed and successful SSH logins
- Detect invalid users
- Aggregate failed attempts by IP
- Sort IPs by number of attempts
- Highlight:
  - Suspicious activity (20+ attempts)
  - Brute-force attacks (50+ attempts)
- Flexible time filtering via `journalctl`

---

## Example Output:

<img width="860" height="1156" alt="image" src="https://github.com/user-attachments/assets/2d4006c8-6ba8-4e58-841d-9453edc1f1f0" />


---

## Requirements

- Linux system with `journalctl`
- Python 3

---

## Installation

```bash
git clone https://github.com/yourname/ssh_log_analyzer.git
cd ssh_log_analyzer

## How to run (examples)::
sudo python3 analyzer.py 30 minutes ago
sudo python3 analyzer.py 2 hours ago
sudo python3 analyzer.py 1 day ago
