import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import PyPDF2
import pikepdf
import threading
import itertools
import string
from concurrent.futures import ThreadPoolExecutor

# Encrypt PDF Function
def encrypt_pdf(input_pdf, output_pdf, password):
    try:
        with open(input_pdf, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            writer.encrypt(password)

            with open(output_pdf, 'wb') as out_file:
                writer.write(out_file)

        messagebox.showinfo("Success", f"Encrypted PDF saved as:\n{output_pdf}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to encrypt PDF:\n{e}")

# Decrypt PDF Functions
def generate_passwords(chars, min_length, max_length):
    for length in range(min_length, max_length + 1):
        for password in itertools.product(chars, repeat=length):
            yield ''.join(password)

def load_passwords(wordlist_file):
    with open(wordlist_file, 'r') as file:
        for line in file:
            yield line.strip()

def try_password(pdf_file, password):
    try:
        with pikepdf.open(pdf_file, password=password):
            return password
    except pikepdf._core.PasswordError:
        return None

def decrypt_pdf(pdf_file, passwords, total_passwords, max_workers, output_label):
    def run():
        output_label.config(text="Trying passwords...")
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_password = {executor.submit(try_password, pdf_file, pwd): pwd for pwd in passwords}
            for i, future in enumerate(future_to_password):
                result = future.result()
                if result:
                    output_label.config(text=f"Password found: {result}")
                    return
                output_label.config(text=f"Tried {i+1}/{total_passwords} passwords")
        output_label.config(text="Password not found in wordlist.")

    threading.Thread(target=run).start()

# GUI Setup
root = tk.Tk()
root.title("PDF Protector & Cracker")
root.geometry("600x500")

notebook = ttk.Notebook(root)
frame_encrypt = ttk.Frame(notebook)
frame_decrypt = ttk.Frame(notebook)
notebook.add(frame_encrypt, text="Encrypt PDF")
notebook.add(frame_decrypt, text="Decrypt PDF")
notebook.pack(expand=True, fill='both')

# Encrypt Tab
input_file_enc = tk.StringVar()
output_file_enc = tk.StringVar()
password_enc = tk.StringVar()

def browse_input_pdf():
    file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file:
        input_file_enc.set(file)
        output_file_enc.set(file.replace(".pdf", "_encrypted.pdf"))

tk.Label(frame_encrypt, text="Select PDF to Encrypt:").pack(pady=5)
tk.Entry(frame_encrypt, textvariable=input_file_enc, width=60).pack()
tk.Button(frame_encrypt, text="Browse", command=browse_input_pdf).pack(pady=2)

tk.Label(frame_encrypt, text="Set Password:").pack(pady=5)
tk.Entry(frame_encrypt, textvariable=password_enc, show="*").pack()

tk.Label(frame_encrypt, text="Output PDF Name:").pack(pady=5)
tk.Entry(frame_encrypt, textvariable=output_file_enc, width=60).pack()

tk.Button(frame_encrypt, text="Encrypt PDF", command=lambda: encrypt_pdf(input_file_enc.get(), output_file_enc.get(), password_enc.get())).pack(pady=10)

# Decrypt Tab
input_file_dec = tk.StringVar()
wordlist_file = tk.StringVar()
use_bruteforce = tk.BooleanVar()
min_length = tk.IntVar(value=1)
max_length = tk.IntVar(value=3)
charset = tk.StringVar(value=string.ascii_lowercase)
max_workers = tk.IntVar(value=4)
status_label = tk.Label(frame_decrypt, text="", wraplength=500, fg="blue")


def browse_protected_pdf():
    file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file:
        input_file_dec.set(file)

def browse_wordlist():
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file:
        wordlist_file.set(file)

def start_decryption():
    pdf = input_file_dec.get()
    if not pdf:
        messagebox.showerror("Missing File", "Please select a PDF file.")
        return

    if use_bruteforce.get():
        pwds = generate_passwords(charset.get(), min_length.get(), max_length.get())
        total = sum(1 for _ in generate_passwords(charset.get(), min_length.get(), max_length.get()))
    else:
        wordlist = wordlist_file.get()
        if not wordlist:
            messagebox.showerror("Missing Wordlist", "Please select a wordlist file.")
            return
        pwds = load_passwords(wordlist)
        total = sum(1 for _ in load_passwords(wordlist))

    decrypt_pdf(pdf, pwds, total, max_workers.get(), status_label)

# GUI elements for Decryption
tk.Label(frame_decrypt, text="Select Encrypted PDF:").pack(pady=5)
tk.Entry(frame_decrypt, textvariable=input_file_dec, width=60).pack()
tk.Button(frame_decrypt, text="Browse PDF", command=browse_protected_pdf).pack(pady=2)

tk.Checkbutton(frame_decrypt, text="Use Brute-force (disable wordlist)", variable=use_bruteforce).pack(pady=5)

brute_frame = tk.Frame(frame_decrypt)
tk.Label(brute_frame, text="Charset:").grid(row=0, column=0)
tk.Entry(brute_frame, textvariable=charset, width=30).grid(row=0, column=1)
tk.Label(brute_frame, text="Min Length:").grid(row=1, column=0)
tk.Entry(brute_frame, textvariable=min_length, width=5).grid(row=1, column=1)
tk.Label(brute_frame, text="Max Length:").grid(row=2, column=0)
tk.Entry(brute_frame, textvariable=max_length, width=5).grid(row=2, column=1)
brute_frame.pack(pady=5)

tk.Label(frame_decrypt, text="Or select Wordlist file:").pack(pady=5)
tk.Entry(frame_decrypt, textvariable=wordlist_file, width=60).pack()
tk.Button(frame_decrypt, text="Browse Wordlist", command=browse_wordlist).pack(pady=2)







tk.Label(frame_decrypt, text="Max Threads:").pack()
tk.Entry(frame_decrypt, textvariable=max_workers, width=5).pack()
tk.Button(frame_decrypt, text="Start Decryption", command=start_decryption).pack(pady=10)
status_label.pack(pady=10)

root.mainloop()