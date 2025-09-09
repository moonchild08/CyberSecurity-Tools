# 🔍 Port Scanner
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

## Usage
Run the script:
python port_scanner.py

## Output
<img width="940" height="312" alt="image" src="https://github.com/user-attachments/assets/8f652886-b0a1-46d0-9544-3f6c0e93a469" />

## Future Improvements

1. Add UDP scanning support
2. Integration with GUI
