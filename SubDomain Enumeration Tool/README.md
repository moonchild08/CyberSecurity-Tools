# SubDomain Enumeration Tool
It is a tool that is use in CyberSecurity and ethical hacking in order to identify valid subdomains associated with a main domain (e.g., finding mail.example.com, shop.example.com, etc., when given example.com).

## 🔍 Purpose of Subdomain Enumeration
1. Information Gathering (Reconnaissance): It helps in discovering the attack surface of a target website.
2. Identify Hidden Services: Some subdomains may not be publicly listed but may host admin panels, dev servers, APIs, etc.
3. Vulnerability Assessment: Different subdomains might be running different technologies or outdated software that could be exploited.

## 🔧 How the Code Works (Logic Only)
#### 1. User Input Handling:
-> Accepts a domain name from the user (e.g., youtube.com).
#### 2. Subdomain Enumeration:
-> Loads a list of potential subdomain names from subdomains.txt.\
-> For each subdomain, sends an HTTP request to http://\<subdomain\>.\<domain\>.\
-> If a valid response is received, the subdomain is considered discovered and stored.
#### 3. DNS Record Lookup:
-> Uses the dnspython library to fetch multiple types of DNS records:\
	=> A (IPv4)
	=> AAAA (IPv6)
	=> CNAME (Canonical Name)
	=> MX (Mail Exchange)
	=> TXT (Text records)
	=> SOA (Start of Authority)\
-> Results are logged for each type if available.
#### 5. Mail Server Connectivity Check:
-> For each discovered MX record, attempts to connect to common mail ports:\
	=> Port 25 (SMTP)
	=> Port 465 (SMTPS)
	=> Port 587 (Submission)\
-> Uses the socket module to test if the port is open.
#### 6. Report Generation:
-> All logs (subdomains, DNS records, mail server checks) are collected.\
-> A timestamped text file is created: domain_YYYYMMDD_HHMM.txt.\
-> The full report is saved in that file for future reference.


