# 🔐 Advanced SSH Brute-Force Tool
A multithreaded SSH brute-force tool built with Python.
It can brute-force SSH credentials using usernames + password lists or generate passwords on-the-fly with configurable length and character sets.

## Features
1. Supports:\
   1.1 Single username (-u)\
   1.2 Username list file (-U)\
   1.3 Password list file (-P)\
   1.4 On-the-fly password generation (--generate)
2. Password generation supports:\
   2.1 Minimum and maximum length (--min_length, --max_length)\
   2.2 Custom character set (--chars)\
   2.3 Multithreaded brute force (--threads) for faster attempts
3. Retries connections in case of temporary SSH lockouts
4. Suppresses unnecessary error logs
5. Saves valid credentials to credentials.txt

## Tech Stack
1. Python 3
2. Paramiko\
 (SSH handling)
3. Colorama\
 (colored output)

### Install dependencies:
pip install paramiko colorama

## Usage
1️⃣ Wordlist Attack (Single Username)
python ssh_bruteforce.py <host> -u root -P passwords.txt

2️⃣ Wordlist Attack (Multiple Usernames)
python ssh_bruteforce.py <host> -U users.txt -P passwords.txt

3️⃣ Password Generation Attack
python ssh_bruteforce.py <host> -u admin --generate --min_length 3 --max_length 5 --chars abc123

4️⃣ Multi-threaded Attack
python ssh_bruteforce.py <host> -u root -P passwords.txt --threads 10

### Example Output
<img width="617" height="255" alt="image" src="https://github.com/user-attachments/assets/afa300f5-de5c-4827-846e-6afdce2e046d" />



### Valid credentials will be saved in:

credentials.txt


#⚠️ Disclaimer

This project is for educational and authorized penetration testing only.
Do not use it on networks or systems without explicit permission.
Unauthorized use may violate laws and result in serious consequences.
