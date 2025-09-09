# 🦹 Information Stealer

This project demonstrates how saved credentials, clipboard content, and basic system information can be programmatically accessed on a local machine.  


---
## Features
- Extract saved browser credentials (from Chrome local database).
- Decrypt stored passwords using Windows API & AES keys.
- Capture clipboard content.
- Collect system and network information:
  - OS version & architecture
  - Hostname & IP address
  - MAC address
  - Processor details
  - Public IP lookup

---

## How It Works
- **Password extraction:** Reads Chrome’s `Login Data` SQLite database, retrieves encrypted credentials, and decrypts them using the system’s key.
- **Clipboard capture:** Retrieves currently stored clipboard content.
- **System info:** Gathers OS, hardware, and network details for forensic awareness.

---

## 🚀 Usage

1️⃣ Install dependencies:
```bash
pip install pycryptodome pyperclip requests
```

## Output
<img width="1350" height="397" alt="image" src="https://github.com/user-attachments/assets/e51f22da-b313-45e9-bdd7-52aa0958306c" />



⚠️ **Disclaimer:**  
This tool is for **educational and ethical research purposes only**. It must **not** be used for unauthorized access or malicious activity. Use only in controlled environments or with explicit permission.

---
