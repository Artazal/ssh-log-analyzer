# SSH Log Analyzer

CLI tool for analyzing SSH logs on Linux servers and detecting suspicious login activity.

Parses `journalctl` logs, aggregates failed login attempts by IP address, and highlights potential brute-force attacks.

---

## Features

- Count failed and successful SSH login attempts
- Detect invalid users
- Aggregate failed login attempts by IP address
- Sort IPs by number of attempts
- Highlight:
  - Suspicious activity (20+ attempts)
  - Brute-force attacks (50+ attempts)
- Clean tabular output in terminal
- Flexible time filtering via `journalctl`
- Optional JSON report export

---

## Example Output

<img width="864" height="2390" alt="image" src="https://github.com/user-attachments/assets/d8d58d52-17f0-4f5f-8096-2f81429e6737" />


---

## Requirements

- Linux system with `journalctl`
- Python 3.8+

---

## Installation

```bash
git clone https://github.com/yourname/ssh_log_analyzer.git
cd ssh_log_analyzer
pip install -r requirements.txt
```

---

## Usage

### Analyze recent logs

```bash
sudo python3 ssh_log_analyzer.py --last "30 minutes"
sudo python3 ssh_log_analyzer.py --last "2 hours"
sudo python3 ssh_log_analyzer.py --last "1 day"
```

---

### Analyze specific time range

```bash
sudo python3 ssh_log_analyzer.py \
  --since "2026-04-24 10:00:00" \
  --until "2026-04-24 12:00:00"
```

---

### Show top N attacking IPs

```bash
sudo python3 ssh_log_analyzer.py --last "1 day" --top 10
```

---

### Save report to JSON

```bash
sudo python3 ssh_log_analyzer.py --last "1 day" --report report.json
```

---

## Arguments

| Argument   | Description |
|-----------|------------|
| `--last`   | Analyze logs from the last period (e.g. "30m", "2h", "1d") |
| `--since`  | Start time (e.g. "2026-04-24 10:00:00") |
| `--until`  | End time |
| `--top`    | Show top N IPs by failed attempts |
| `--report` | Save results to JSON file |

---

## How It Works

1. Fetches logs using `journalctl`
2. Parses SSH authentication events
3. Extracts IP addresses
4. Aggregates failed login attempts
5. Labels suspicious or brute-force behavior
6. Outputs results in a readable table

---

## Project Structure

```bash
ssh_log_analyzer/
├── ssh_log_analyzer.py
├── tests/
│   └── test_analyzer.py
├── requirements.txt
├── README.md
```

---

## Example JSON Report

```json
{
  "stats": {
    "failed_password": 120,
    "accepted_password": 5,
    "invalid_user": 40
  },
  "ip_analysis": [
    {
      "ip": "192.168.1.1",
      "attempts": 80,
      "label": "Brute force attack"
    }
  ],
  "since": "1 day ago",
  "until": null,
  "top": 10
}
```

---

## Future Improvements

- Configurable thresholds for attack detection
- Support for additional log sources
- Integration with alerting systems
- IP geolocation enrichment

---

## Notes

- Requires root privileges (`sudo`) to access system logs
- Designed for Linux environments using systemd

---

## License

MIT
