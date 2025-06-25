# PDF protection tool  -  PDF Cracker tool

There are two python files-
1. Protection.py and,
2. Cracker.py

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



