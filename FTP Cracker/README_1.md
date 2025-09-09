# 🔑 FTP Brute Force Script 

A simple multithreaded FTP brute-force script written in Python using the `ftplib` library.  
This project is designed **only for ethical use** in penetration testing labs, Capture the Flag (CTF) challenges, or cybersecurity learning environments.  



---

## Features
- Multithreaded password attempts (default: 30 threads).
- Customizable host, port, and username.
- Reads passwords from a wordlist file.
- Displays credentials if login is successful.
- Gracefully stops after finding valid credentials.

---

## How It Works
1. Loads a wordlist from `wordlist.txt`.
2. Each password is queued for brute-forcing.
3. Threads run in parallel, attempting to connect via FTP.
4. On success:
   - Prints valid credentials.
   - Stops further attempts.

---

## Usage

1️⃣ Install dependencies:
```bash
pip install colorama
```


2️⃣ Add your wordlist:\
wordlist.txt


3️⃣ Edit the script:\
commands to be run on target machine(here, kali linux)

```bash
sudo apt install vsftpd -y

sudo systemctl start vsftpd

sudo systemctl startus vsftpd
```





4️⃣ Run the script:\
On the main machine
``` bash 
python ftp_brute.py
```


### Example Output
<img width="940" height="445" alt="image" src="https://github.com/user-attachments/assets/80e418fb-3596-4df9-b59e-c8bdfec002a6" />

<img width="905" height="380" alt="image" src="https://github.com/user-attachments/assets/e2c01413-385c-4578-82f1-bc0d5b1d7658" />

<img width="940" height="445" alt="image" src="https://github.com/user-attachments/assets/2aaecb17-e6e7-4ae3-a5d8-16345e1b31e0" />



## Educational Value
- How FTP authentication works.
  - Risks of weak/default passwords.
  - Basics of multithreading in Python.
  - Why strong passwords and account lockout policies are crucial.



⚠️ **Disclaimer:**  
This script is for **educational and research purposes only**.  
Unauthorized use against systems you do not own or have explicit permission to test is **illegal**.

⚠️ Ethical Use
✅ For students: Learn about brute-force attacks in a safe, controlled environment.

✅ For pentesters: Use in authorized security assessments.

❌ Do not use this tool against systems without permission.
