import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import requests
import dns.resolver
import os
import socket
import datetime

class SubdomainTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Subdomain Enumeration Tool")
        self.root.geometry("700x600")
        self.lock = threading.Lock()
        self.discovered_subdomains = []
        self.domain_name = ""

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter Domain Name (eg: 'abc.com')").pack(pady=5)

        self.domain_entry = tk.Entry(self.root, width=50)
        self.domain_entry.pack(pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.start_button = tk.Button(button_frame, text="Start Enumeration", command=self.start_enumeration)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(button_frame, text="Clear & New Scan", command=self.reset_fields, state=tk.NORMAL)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        self.output_area = scrolledtext.ScrolledText(self.root, width=80, height=30, wrap=tk.WORD)
        self.output_area.pack(padx=10, pady=10)

    def log(self, message):
        self.output_area.after(0, self._append_log, message)

    def _append_log(self, message):
        self.output_area.insert(tk.END, message + '\n')
        self.output_area.see(tk.END)

    def load_subdomains(self):
        if not os.path.exists("subdomains.txt"):
            self.log("❌ Error: subdomains.txt file not found.")
            return []
        with open("subdomains.txt") as f:
            return f.read().splitlines()

    def check_subdomain(self, subdomain, domain):
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url, timeout=2)
        except requests.ConnectionError:
            pass
        else:
            with self.lock:
                self.discovered_subdomains.append(url)
                self.log(f"[+] Found: {url}")

    def run_subdomain_enum(self, domain):
        self.log(f"\n🔍 Starting subdomain enumeration for: {domain}")
        subdomains = self.load_subdomains()
        threads = []
        for sub in subdomains:
            t = threading.Thread(target=self.check_subdomain, args=(sub, domain))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

        self.log(f"\n✅ Done! Discovered {len(self.discovered_subdomains)} subdomains.")

    def check_mail_server_connectivity(self, mx_record):
        ports = [25, 465, 587]
        self.log(f"\n🔌 Checking mail server connectivity for: {mx_record}")
        for port in ports:
            try:
                with socket.create_connection((str(mx_record), port), timeout=5):
                    self.log(f"✅ Port {port} is open on {mx_record}")
            except socket.error:
                self.log(f"❌ Port {port} is closed or unreachable on {mx_record}")

    def run_dns_lookup(self, domain):
        self.log(f"\n🔍 Performing DNS record lookup for: {domain}")
        records_type = ['A', 'AAAA', 'CNAME', 'MX', 'TXT', 'SOA']
        resolver = dns.resolver.Resolver()

        for record_type in records_type:
            try:
                answers = resolver.resolve(domain, record_type)
                if record_type == "MX":
                    self.log(f"\n📬 Mail Servers (MX Records):")
                    mx_hosts = []
                    for data in answers:
                        self.log(f"   - {data.exchange} (Priority: {data.preference})")
                        mx_hosts.append(str(data.exchange).rstrip('.'))

                    for mx in mx_hosts:
                        self.check_mail_server_connectivity(mx)

                else:
                    self.log(f"\n🔹 {record_type} Records:")
                    for data in answers:
                        self.log(f"   - {data}")
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
                continue
            except Exception as e:
                self.log(f"⚠️ Error fetching {record_type} records: {e}")

    def save_full_output(self):
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M')
        filename = f"{self.domain_name}_{timestamp}.txt"
        content = self.output_area.get('1.0', tk.END)
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content.strip())
            self.log(f"\n📝 Full report saved to {filename}")
        except Exception as e:
            self.log(f"❌ Error saving report: {e}")

    def start_enumeration(self):
        domain = self.domain_entry.get().strip().lower()
        self.domain_name = domain.replace('.', '_')

        if not domain or '.' not in domain:
            messagebox.showerror("Invalid Input", "Please enter a valid domain name (e.g., example.com)")
            return

        self.start_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.output_area.insert(tk.END, "\n============= NEW SCAN =============\n")
        self.output_area.see(tk.END)

        threading.Thread(target=self.run_all, args=(domain,)).start()

    def run_all(self, domain):
        self.discovered_subdomains.clear()
        self.run_subdomain_enum(domain)
        self.run_dns_lookup(domain)
        self.save_full_output()

        self.root.after(0, lambda: self.start_button.config(state=tk.NORMAL))
        self.root.after(0, lambda: self.reset_button.config(state=tk.NORMAL))

    def reset_fields(self):
        self.domain_entry.delete(0, tk.END)
        self.output_area.delete('1.0', tk.END)
        self.discovered_subdomains.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = SubdomainTool(root)
    root.mainloop()
