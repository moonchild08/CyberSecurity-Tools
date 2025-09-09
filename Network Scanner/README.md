# 🛰️ Network Scanner

A multithreaded network scanning tool built using Python and Scapy.
This tool discovers all active devices in a given network by sending ARP requests, retrieving their IP, MAC, and Hostname.


## 🚀 Features
1. Scans an entire network using CIDR notation (e.g., 192.168.1.0/24)
2. Fetches:\
   2.1 IP Address\
   2.2 MAC Address\
   2.3 Hostname (if available)
3. Uses multithreading for faster scanning 
4. Clean and formatted output

## 🛠️ Tech Stack

1. Python 3
2. Scapy
3. Socket library (for hostname lookup)
4. Threading

## 📦 Installation

Clone the repository:

git clone https://github.com/your-username/network-scanner.git
cd network-scanner


Install dependencies:
pip install scapy

## ▶️ Usage

Run the script:
python scanner.py
Enter a network range in CIDR format:
Enter network ip address: 192.168.1.0/24

📊 Example Output
IP                   MAC                  Hostname
--------------------------------------------------------------------------------
192.168.1.1          aa:bb:cc:dd:ee:ff    router.local
192.168.1.10         11:22:33:44:55:66    my-laptop
192.168.1.20         77:88:99:aa:bb:cc    Unknown

## 🔮 Future Improvements
1. Export results to CSV/JSON
2. Add port scanning feature
3. GUI support



<img width="943" height="217" alt="image" src="https://github.com/user-attachments/assets/816f5139-4bcb-42ae-a36e-35fc481f09c9" />

