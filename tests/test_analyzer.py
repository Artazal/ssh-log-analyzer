from ssh_log_analyzer import analyze_logs, sort_ips, get_label, positive_int


def test_get_label_brute_force():
    assert get_label(50) == "Brute force attack"

def test_get_label_suspicious():
    assert get_label(20) == "Suspicious"

def test_get_label_empty():
    assert get_label(5) == ""


def test_sort_ips_descending():
    data = {
        "1.1.1.1": 5,
        "2.2.2.2": 20,
        "3.3.3.3": 10
    }

    result = sort_ips(data, None)

    assert result == [
        ("2.2.2.2", 20),
        ("3.3.3.3", 10),
        ("1.1.1.1", 5)
    ]


def test_sort_ips_top_n():
    data = {
        "1.1.1.1": 5,
        "2.2.2.2": 20,
        "3.3.3.3": 10
    }

    result = sort_ips(data, 2)

    assert result == [
        ("2.2.2.2", 20),
        ("3.3.3.3", 10)
    ]


def test_analyze_logs_counts_failed_passwords_by_ip():
    fake_log = """
Apr 25 10:00:00 server sshd[123]: Failed password for root from 1.1.1.1 port 1234 ssh2
Apr 25 10:01:00 server sshd[124]: Failed password for invalid user admin from 1.1.1.1 port 1235 ssh2
Apr 25 10:02:00 server sshd[125]: Failed password for root from 2.2.2.2 port 1236 ssh2
Apr 25 10:03:00 server sshd[126]: Accepted password for ubuntu from 3.3.3.3 port 1237 ssh2
"""

    stats, failed_by_ip = analyze_logs(fake_log)

    assert stats["failed_password"] == 3
    assert stats["accepted_password"] == 1
    assert failed_by_ip["1.1.1.1"] == 2
    assert failed_by_ip["2.2.2.2"] == 1


import pytest
import argparse

def test_positive_int_valid():
    assert positive_int("10") == 10

def test_positive_int_zero_raises_error():
    with pytest.raises(argparse.ArgumentTypeError):
        positive_int("0")

def test_positive_int_negative_raises_error():
    with pytest.raises(argparse.ArgumentTypeError):
        positive_int("-5")
