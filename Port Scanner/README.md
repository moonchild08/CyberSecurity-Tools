🔍 Port Scanner
A fast multithreaded TCP port scanner built in Python.
This tool scans a target host for open ports, detects running services, and grabs service banners if available.

## Features

1. Scans a given host over a range of ports
2. Detects:
   2.1 Running services (via socket.getservbyport)\
   2.2 Service banners (if available)\
   2.3 Uses concurrent threads for high-speed scanning\
3. Progress indicator for better user experience
4. Color-coded terminal output (open ports in red, banners in green)

## Tech Stack
1. Python 3
2. Built-in libraries:
3. socket
4. concurrent.futures
   sys

📦 Installation

Clone the repository:

git clone https://github.com/your-username/port-scanner.git
cd port-scanner


No external dependencies required 🎉

▶️ Usage

Run the script:

python port_scanner.py


Enter details when prompted:

Enter your target ip: 192.168.1.1
Enter the start port: 1
Enter end port: 1024

📊 Example Output
Starting scan on host: 192.168.1.1
Progress: 1024/1024 ports scanned

Port Scan Results:
Port     Service         Status
-------------------------------------------------------------------------------------
22       ssh             Open
          SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.7
80       http            Open
          HTTP/1.1 400 Bad Request
443      https           Open

⚡ Future Improvements

Add UDP scanning support
Integration with GUI
