# 🔐 SSH Brute-Force Tool
A Python-based SSH brute-force script that attempts to log in to a target host using a username and a list of passwords.
Built with Paramiko, it automates the process of testing multiple credentials against an SSH server.

## Features
1. Tries multiple passwords from a given wordlist against an SSH server
2. Handles:\
   2.1 Connection timeouts\
   2.2 Authentication failures\
   2.3 Temporary lockouts (retries after delay)
3. Saves valid credentials to credentials.txt
4. Color-coded terminal output (success in green, errors in red/blue)

## Tech Stack
1. Python 3
2. Paramiko\
 (SSH handling)
3. Colorama\
 (colored output)

### Install dependencies:
pip install paramiko colorama

## Usage

Run the script:\
python ssh_bruteforce.py <host> -u <username> -P <password_list>

Example:\
python ssh_bruteforce.py 192.168.1.10 -u root -P rockyou.txt

### Example Output

-> Testing from Windows 11 (Host) to Kali Linux (Virtual Machine)
<img width="940" height="303" alt="image" src="https://github.com/user-attachments/assets/2f437ce7-5a56-4cd3-9c6c-178045c527d0" />
<img width="940" height="445" alt="image" src="https://github.com/user-attachments/assets/e6823a9f-a693-44a3-abda-df341c79b032" />


### 👉 If successful, the credentials will be saved to:

credentials.txt

example content:\
root@192.168.1.10:toor

## Future Improvements
1. Add multi-threading for faster brute force
2. Support for username lists
3. Integrate with proxy chains / TOR for anonymity
4. Add logging & reporting features


# ⚠️ Disclaimer
This project is for educational and ethical testing purposes only.
Do not use it on networks or systems without explicit authorization.
Unauthorized use may violate laws and result in serious consequences.
