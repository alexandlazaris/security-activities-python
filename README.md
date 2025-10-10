# scapy-doo

## Install

1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`


## What have we learned:
- lesson_1: `packet_reader.py` -> read a packet file, disect packets within, build our own packets ✅
- lesson_2: `port_scan.py` -> scan a list of ports, check for open ports + print results ✅
- lesson_3: `dns_exploration.py` -> scan & discover domains & ips using dns request + reverse dns requests ✅
- lesson_4: `check_default_credentials.py` -> brute force logins using a predefined list of username + password combos against ssh & telnet servers running on localhost ✅
- lesson_5: use `pyinstaller` to package malicious python scripts as executables, targeting the Autorun feature of older Windows versions ✅
- lesson_6: create a fake login page to phish for user credentials ✅
- lesson_7: TBC
- lesson_8: TBC
- lesson_9: hijack execution flows by cloning & manipulation path/alias variables ✅
- lesson_10: add generated .exes to Windows Registry, allowing malicious software to run on Logon ✅
- lesson_11: hijacks the python library search order to instead invoke a fake library ✅


## Data sources

- Wireshark sample packets: https://wiki.wireshark.org/samplecaptures#sample-captures

## Tools used

- [Orbstack](https://orbstack.dev/): whip up lightweight virtual Linux machines to test out scripts or run ssh connections