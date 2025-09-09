# CyberSecurity-Tools


## 1. **Network & Port Scanning Projects**

### **a) Network Scanner**

* **Purpose:** Identify all devices connected to a network and gather their IP, MAC addresses, and hostnames.
* **Key Features:**

  * Uses `ARP` requests to discover devices.
  * Multi-threaded for faster scanning.
  * Resolves hostnames for connected devices.
  * Outputs a clean table of results.
* **Use Case:** Network administration, discovering unauthorized devices, pentesting LANs.

### **b) Port Scanner**

* **Purpose:** Scan a target host to find open TCP ports and services.
* **Key Features:**

  * Multi-threaded scanning using `concurrent.futures`.
  * Retrieves service names for known ports.
  * Attempts to read banners for open ports.
  * Shows progress in real-time and formats results nicely.
* **Use Case:** Security auditing, identifying vulnerable open ports, pentesting.

---

## 2. **Hash Cracking Project**

### **Hash Cracker**

* **Purpose:** Recover original passwords from cryptographic hashes (e.g., MD5, SHA variants).
* **Key Features:**

  * Supports wordlists and brute-force generation.
  * Multi-threaded for faster cracking.
  * Supports hash types: MD5, SHA1, SHA256, SHA512, SHA3 variants, etc.
  * Real-time progress display with `tqdm`.
* **Use Case:** Password recovery, security testing, analyzing weak passwords.

---

## 3. **SSH Brute Force Projects**

### **a) Simple SSH Brute Force**

* **Purpose:** Test SSH login credentials for a single user.
* **Key Features:**

  * Takes a host IP and a password list.
  * Writes successful credentials to `credentials.txt`.
  * Single-threaded for simplicity.

### **b) Advanced SSH Brute Force**

* **Purpose:** Brute force SSH using multiple users, passwords, or password generation.
* **Key Features:**

  * Multi-threaded with queue system.
  * Supports usernames from a file or a single user.
  * Passwords from a file or generated on the fly.
  * Retries on SSH exceptions with exponential backoff.
  * Logs successful credentials.
* **Use Case:** Security auditing of SSH servers, pentesting.

---

## 4. **FTP Brute Force Projects**

### **a) Basic FTP Brute Force**

* **Purpose:** Test login credentials on a fixed FTP server.
* **Key Features:**

  * Single target host, username, and port.
  * Passwords loaded from a wordlist.
  * Multi-threaded for faster attempts.
  * Color-coded success/failure output.

### **b) Advanced FTP Brute Force**

* **Purpose:** Fully customizable FTP brute force.
* **Key Features:**

  * Multi-threaded.
  * Supports single or multiple users.
  * Passwords from wordlists or generated dynamically.
  * Customizable character sets, length, and number of threads.
  * Stops threads automatically when credentials are found.
* **Use Case:** FTP server security auditing.

---

## 5. **Reverse Shell Projects**

### **Reverse Shell (client.py & server.py)**

* **Purpose:** Provides remote access from a client to a server over TCP.
* **Key Features:**

  * Execute commands remotely.
  * Supports file upload/download via Base64 encoding.
  * Persistent reconnection on the client side.
  * Handles directory changes (`cd`) and exit commands.
* **Use Case:** Educational demonstrations of reverse shells and remote administration (authorized pentesting only).

---

## 6. **Information Stealer Project**

### **Browser Password & System Info Stealer**

* **Purpose:** Extract sensitive data like saved browser passwords, clipboard content, and system information.
* **Key Features:**

  * Decrypts Chrome saved passwords using system cryptography.
  * Captures clipboard contents.
  * Collects system info (hostname, IP, MAC, OS, architecture).
  * Fetches global IP address via API.
* **Use Case:** Educational, demonstrating how sensitive information can be exposed. *(Use ethically)*

---

## 7. PDF Protector & Cracker

* **Purpose:** Encrypt and decrypt PDF files.

* **Features:**
  * PDF encryption with user-defined password.
  * Decryption via:
     * Wordlist attack.
     * Brute-force attack with customizable charset, min/max length.
  * Multi-threaded password attempts for speed.
  * GUI using Tkinter with clear tabs for encrypt/decrypt operations.
* **Use Case:** Demonstrates file security concepts and password recovery techniques.

---

## 8. Subdomain Enumeration & DNS Tool

* **Purpose:** Gather information about a domain for reconnaissance.

* **Features:**
  * Subdomain enumeration using a wordlist.\
  * DNS lookup for A, AAAA, CNAME, MX, TXT, SOA records.
  * Mail server port checking (25, 465, 587).
  * GUI with live logging of results.
  * Full scan report saved with timestamp.
* **Use Case:** Useful for ethical hacking and security assessments of domains.

---

### **Summary Table of Projects**

| Project Type             | Project Name                  | Functionality                                                                                      |
| ------------------------ | ----------------------------- | -------------------------------------------------------------------------------------------------- |
| Network Scanning         | Network Scanner               | Find devices in LAN, get IP/MAC/Hostname                                                           |
| Network Scanning         | Port Scanner                  | Scan open ports, services, banners                                                                 |
| Password Cracking        | Password Cracker              | Recover passwords from hashes using wordlists/brute-force                                          |
| SSH Brute Force          | Simple SSH Brute              | Single user/password list SSH brute force                                                          |
| SSH Brute Force          | Advanced SSH Brute            | Multi-user, multi-password, generated passwords, multi-threaded                                    |
| FTP Brute Force          | Basic FTP Brute               | Single user/host FTP brute force                                                                   |
| FTP Brute Force          | Advanced FTP Brute            | Multi-user, password generation, threads, flexible                                                 |
| Remote Access            | Reverse Shell                 | Remote command execution, file transfer                                                            |
| Info Stealer             | Information Stealer           | Extract browser passwords, clipboard content, system info                                          |
| PDF Protection & Cracker | PDF Protector & Cracker       | Encrypt PDF files with password, decrypt using wordlist or brute-force                             |
| Reconnaissance/Domain    | Subdomain Enumeration Tool    | Enumerate subdomains, perform DNS record lookup (A, AAAA, MX, CNAME, TXT, SOA), check mail servers |

---

