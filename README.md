# ssh-log-analyzer
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

Analyzing logs since: 30 hours ago

Log analysis result:
failed_password: 5111
accepted_password: 8
invalid_user: 4910
error: 5
warning: 0

Failed password attempts from IP:

45.33.72.158: 685 Brute force attack
87.251.64.147: 359 Brute force attack
87.251.64.144: 329 Brute force attack
87.251.64.145: 329 Brute force attack
87.251.64.149: 328 Brute force attack
2.57.122.191: 125 Brute force attack
45.227.254.170: 120 Brute force attack
2.57.121.112: 115 Brute force attack
2.57.121.25: 110 Brute force attack
92.118.39.236: 110 Brute force attack
213.209.159.159: 110 Brute force attack
2.57.122.190: 105 Brute force attack
2.57.122.195: 105 Brute force attack
193.32.162.151: 101 Brute force attack
2.57.122.193: 95 Brute force attack
92.118.39.195: 95 Brute force attack
195.178.110.15: 95 Brute force attack
2.57.122.196: 95 Brute force attack
2.57.122.189: 90 Brute force attack
2.57.122.199: 90 Brute force attack
45.148.10.151: 90 Brute force attack
92.118.39.23: 85 Brute force attack
2.57.122.197: 85 Brute force attack
2.57.122.192: 85 Brute force attack
92.118.39.235: 85 Brute force attack
45.148.10.157: 80 Brute force attack
182.93.7.194: 78 Brute force attack
92.118.39.196: 65 Brute force attack
92.118.39.197: 65 Brute force attack
45.148.10.141: 65 Brute force attack
193.32.162.145: 65 Brute force attack
45.148.10.147: 55 Brute force attack
2.57.122.194: 50 Brute force attack
80.94.92.186: 50 Brute force attack
138.68.106.123: 44 Suspicious
80.94.92.182: 40 Suspicious
45.148.10.152: 35 Suspicious
2.57.122.238: 31 Suspicious
103.147.159.91: 26 Suspicious
5.182.83.231: 26 Suspicious
90.169.216.25: 26 Suspicious
61.231.228.53: 26 Suspicious
120.48.140.232: 26 Suspicious
171.25.158.82: 26 Suspicious
102.88.137.213: 26 Suspicious
77.53.234.151: 22 Suspicious
159.89.31.79: 22 Suspicious
196.119.130.247: 22 Suspicious
45.148.10.121: 19
36.133.163.5: 16
179.124.29.29: 16
124.71.5.84: 12
101.132.144.220: 11
45.148.10.183: 6
106.13.165.101: 6
120.133.52.228: 5
118.145.164.82: 4
180.76.105.108: 4
80.94.92.168: 3
172.245.16.13: 3
121.29.4.46: 3
68.126.61.81: 3
118.145.246.44: 2
193.142.146.230: 2
213.169.44.220: 1

---

## Requirements

- Linux system with `journalctl`
- Python 3

---

## Installation

```bash
git clone https://github.com/yourname/ssh-log-analyzer.git
cd ssh-log-analyzer

## How to run (examples)::
sudo python3 analyzer.py 30 minutes ago
sudo python3 analyzer.py 2 hours ago
sudo python3 analyzer.py 1 day ago
