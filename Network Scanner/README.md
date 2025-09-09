# 🛰️ Network Scanner

A multithreaded network scanning tool built using Python and Scapy.
This tool discovers all active devices in a given network by sending ARP requests, retrieving their IP, MAC, and Hostname.


## Features
1. Scans an entire network using CIDR notation (e.g., 192.168.1.0/24)
2. Fetches:\
   2.1 IP Address\
   2.2 MAC Address\
   2.3 Hostname (if available)
3. Uses multithreading for faster scanning 
4. Clean and formatted output

## Tech Stack

1. Python 3
2. Scapy
3. Socket library (for hostname lookup)
4. Threading


### Install dependencies: 
pip install scapy

## Usage

Run the script:
python scanner.py
Enter a network range in CIDR format:
Enter network ip address: 192.168.1.0/24


## Example Output
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IP&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MAC&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hostname 

--------------------------------------------------------------------------------

192.168.1.1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;aa:bb:cc:dd:ee:ff&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router.local

192.168.1.10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;11:22:33:44:55:66&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;my-laptop

192.168.1.20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;77:88:99:aa:bb:cc&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unknown

## Future Improvements
1. Export results to CSV/JSON
2. Add port scanning feature
3. GUI support



<img width="943" height="217" alt="image" src="https://github.com/user-attachments/assets/816f5139-4bcb-42ae-a36e-35fc481f09c9" />

