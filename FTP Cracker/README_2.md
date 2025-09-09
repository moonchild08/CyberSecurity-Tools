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
<img width="283" height="216" alt="image" src="https://github.com/user-attachments/assets/d779588a-9c86-498b-94cd-50217359c5b6" />

<img width="940" height="186" alt="image" src="https://github.com/user-attachments/assets/c675bf34-968e-46aa-9657-7c2757b19ff2" />

<img width="940" height="244" alt="image" src="https://github.com/user-attachments/assets/c3cfbbd5-d995-4fa5-89e1-d7f60146c0c5" />



## Educational Value
- How FTP authentication works.
  - Risks of weak/default passwords.
  - Basics of multithreading in Python.
  - Why strong passwords and account lockout policies are crucial.


---
⚠️ **Disclaimer:**  
This script is for **educational and research purposes only**.  
Unauthorized use against systems you do not own or have explicit permission to test is **illegal**.

