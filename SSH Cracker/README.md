🔐 SSH Brute-Force Tool

A Python-based SSH brute-force script that attempts to log in to a target host using a username and a list of passwords.
Built with Paramiko, it automates the process of testing multiple credentials against an SSH server.

⚠️ Disclaimer

This project is for educational and ethical testing purposes only.
Do not use it on networks or systems without explicit authorization.
Unauthorized use may violate laws and result in serious consequences.

🚀 Features

Tries multiple passwords from a given wordlist against an SSH server

Handles:

Connection timeouts

Authentication failures

Temporary lockouts (retries after delay)

Saves valid credentials to credentials.txt

Color-coded terminal output (success in green, errors in red/blue)

🛠️ Tech Stack

Python 3

Paramiko
 (SSH handling)

Colorama
 (colored output)

📦 Installation

Clone the repository:

git clone https://github.com/your-username/ssh-bruteforce.git
cd ssh-bruteforce


Install dependencies:

pip install paramiko colorama

▶️ Usage

Run the script:

python ssh_bruteforce.py <host> -u <username> -P <password_list>

Example:
python ssh_bruteforce.py 192.168.1.10 -u root -P rockyou.txt

📊 Example Output
[-] Invalid credentials for root:123456
[-] Invalid credentials for root:password
[-] Invalid credentials for root:qwerty
Found combo: 
    HOSTNAME: 192.168.1.10
    USERNAME: root
    PASSWORD: toor


👉 If successful, the credentials will be saved to:

credentials.txt


Example content:

root@192.168.1.10:toor

⚡ Future Improvements

Add multi-threading for faster brute force

Support for username lists

Integrate with proxy chains / TOR for anonymity

Add logging & reporting features

🤝 Contributing

Feel free to fork and submit pull requests. Suggestions are welcome!
