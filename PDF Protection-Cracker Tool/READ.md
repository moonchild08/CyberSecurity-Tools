# PDF protection tool  -  PDF Cracker tool
The **PDF_Protection_Cracker_tool.py** python file is a combination of two python scripts that are - 
1. Protection.py and,
2. Cracker.py respectively.

But this file is a Python-based GUI application that allows you to:

* **Encrypt** any PDF with a custom password.
* **Decrypt** password-protected PDFs using either:
  * A **wordlist dictionary attack**
  * A **brute-force password generator** with customizable character sets and lengths

---

### 🚀 Features

#### PDF Encryption

* Select a PDF file from your system
* Set a password
* Instantly generate a secure, password-protected PDF

#### PDF Decryption

* **Option 1: Wordlist Attack**

  * Upload a `.txt` wordlist file (one password per line)
  * Multi-threaded cracking for speed
* **Option 2: Brute-force Attack**

  * Set character set (letters, digits, symbols, etc.)
  * Choose min & max password length
  * Fully automated generation and testing
* Live status updates inside the GUI

---

### 🛠 Built With

* `Tkinter` – for GUI design
* `PyPDF2` – for PDF encryption
* `pikepdf` – for PDF decryption
* `ThreadPoolExecutor` – for fast, concurrent cracking
* `itertools` & `string` – for brute-force password generation

---

### 📦 Requirements

Install the dependencies using:

```bash
pip install PyPDF2 pikepdf
```

---

### 📂 How to Use

1. **Run the GUI:**

```bash
python PDF_Protection_Cracker_tool.py
```

2. Choose between **Encrypt** or **Decrypt** tabs
3. Follow the on-screen fields and buttons
4. Password found during decryption will be shown in real-time

---

### 📁 Example Wordlist Format

Each password should be in a new line:

```
1234
password
letmein
secret
```

---

### 🧩 Future Add-ons (optional ideas)

* Export cracked/decrypted PDF directly
* Save password attempt logs
* Embed a graphical progress bar
* Package as `.exe` using `pyinstaller`


![Screenshot 2025-06-26 012741](https://github.com/user-attachments/assets/9d72431e-f914-44fe-b8fd-36d3e3d0001f)
![Screenshot 2025-06-26 012754](https://github.com/user-attachments/assets/97b56203-616c-4252-8898-a527d3a8abf4)
![Screenshot 2025-06-26 012855](https://github.com/user-attachments/assets/a50c73af-e145-4c01-9c5d-602d5f71dad7)
![image](https://github.com/user-attachments/assets/d3a3eb30-8078-4c59-ad0b-e9ef856cdd4e)
![image](https://github.com/user-attachments/assets/2f7f6d15-1989-4294-ad98-66a9b4263c1b)















## Now

The above python file is a combination of two python scripts that are - 
1. Protection.py and,
2. Cracker.py respectively.

Both the files does different jobs. 

Here’s a **basic summary** of what each script does:

---

### 🛡️ `protection.py` – *PDF Password Protection Script*

**Purpose:**
Adds a **password** to an existing PDF file to protect it from unauthorized access.

**What it does:**

* Takes an input PDF file.
* Copies all pages into a new PDF.
* Encrypts the new PDF with a given password.
* Saves the result as a password-protected PDF.

**Use Case:**
You use this when you want to **secure a PDF** with a password before sharing or storing it.

---

### 🔓 `cracker.py` – *PDF Password Cracker Script*

**Purpose:**
Tries to **unlock** a password-protected PDF by guessing the password using:

* A **wordlist** (list of possible passwords), or
* **Dynamically generated** passwords (brute-force).

**What it does:**

* Takes a protected PDF file.
* Tries every password from the list or generator.
* Uses **multi-threading** to speed up the cracking process.
* Stops and prints the password if found.

**Use Case:**
You use this when you have a locked PDF and:

* Forgot the password, or
* Want to test the strength of the password.



