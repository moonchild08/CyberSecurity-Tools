# FTP Brute Force (Basic)

A **multithreaded FTP brute force script** written in Python using the built-in `ftplib`.
This basic version works with a **single target, fixed username, and a wordlist file**.

---

## Features

* Attempts FTP login with a **fixed user** (`bhavana`)
* Loads passwords from a wordlist file (`wordlist.txt`)
* Uses 30 threads for faster cracking
* Color-coded output with `colorama`

---

## Usage

1. Place your password wordlist in a file named **`wordlist.txt`**

2. Update the script with your:

   * **Target host/IP** (`host`)
   * **Username** (`user`)
   * **Port** (default: 21)

3. Run the script:

```bash
python ftp_brute_basic.py
```

---

## Output
<img width="940" height="445" alt="image" src="https://github.com/user-attachments/assets/5edcc3f3-c6fd-4984-9561-d3867f4fa8e8" />

<img width="855" height="355" alt="image" src="https://github.com/user-attachments/assets/b9b7e303-dc7a-43d8-bd78-f1bc9894d19d" />

<img width="940" height="445" alt="image" src="https://github.com/user-attachments/assets/f844c9f0-9046-4848-b359-229dea7a7c33" />

<img width="940" height="445" alt="image" src="https://github.com/user-attachments/assets/17b25407-2caa-444f-84b2-f3bbbab8e4cc" />

---

## Requirements

* Python 3.x
* `colorama`

Install with:

```bash
pip install colorama
```

---
⚠️ **Disclaimer:** This project is for **educational and penetration testing purposes only**.
Do not use it against systems without **explicit authorization**.

