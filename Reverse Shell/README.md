# 🔄 Python Reverse Shell

This project demonstrates a simple **reverse shell** written in Python.  
It allows a remote server to execute commands on a client machine, as well as upload/download files between them.

⚠️ **Disclaimer:** This tool is for **educational purposes only**. Do **NOT** use it for unauthorized access or malicious activity. Use only in controlled environments where you have explicit permission.

---

## 📂 Project Structure
reverse-shell\
│── client.py # Runs on the victim machine (connects back to server)\
│── server.py # Runs on the attacker's machine (controls the client)


---

## ⚙️ Features
- Remote command execution (interactive shell).
- File upload & download (base64 encoded).
- Directory navigation (`cd` command).
- Persistent connection retries if server is unavailable.

---

## 🚀 Usage

### 1️⃣ Start the Server
On your **attacker machine**:
```bash
python server.py
```

This starts a listener that waits for incoming client connections.

### 2️⃣ Run the Client

On the target machine (with IP changed to server’s IP):

```bash
python client.py
```


### Example Commands

From the server.py shell:

ls → list files

pwd → print working directory

cd <directory> → change directory

download <filename> → download a file from client

upload <filename> → upload a file to client

exit → close connection

# Ethical Notice

This project is for:

Learning about network security

Understanding reverse shell mechanics

Practicing incident detection & response

❌ Do NOT use this on systems you do not own or without permission. Unauthorized usage may be illegal.
