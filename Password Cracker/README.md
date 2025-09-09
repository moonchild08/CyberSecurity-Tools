# 🔑 Hash Cracker
A multithreaded hash cracking tool built with Python.
It supports dictionary attacks (wordlist-based) and brute-force attacks (password generation with customizable length & character sets).

## Features
1. Supports multiple hash algorithms:\
   1.1 md5, sha1, sha224, sha256, sha384, sha512\
   1.2 sha3_224, sha3_256, sha3_384, sha3_512
2. Two attack modes:\
   2.1 Wordlist attack – try passwords from a given wordlist file\
   2.2 Brute-force attack – generate all possible combinations within a given length range
3. Multithreaded (using ThreadPoolExecutor) for faster performance
4. Progress tracking with tqdm
5. Customizable:\
   5.1 Password length (min_length, max_length)\
   5.2 Character set (ascii_letters, digits, or custom set)
   5.3 Number of worker threads

## Tech Stack
1. Python 3
2. Built-in libraries: hashlib, itertools, string, argparse, concurrent.futures
3. External library: tqdm
 for progress bar

### Install dependencies:
pip install tqdm

## Usage
### Wordlist Attack
python hash_cracker.py <hash> -w wordlist.txt --hash_type sha256


Example:

python hash_cracker.py e3afed0047b08059d0fada10f400c1e5 -w rockyou.txt --hash_type md5

🔨 Brute-force Attack
python hash_cracker.py <hash> --hash_type sha1 --min_length 3 --max_length 5 -c abc123


Example:

python hash_cracker.py 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8 --hash_type sha1 --min_length 3 --max_length 6 -c abcdef123

📊 Example Output
<img width="940" height="206" alt="image" src="https://github.com/user-attachments/assets/bb4817be-b13d-47fb-9ee3-958f717e8ac7" />


 ## Future Improvements
1. Add GPU acceleration (via CUDA / OpenCL)
2. Support for rainbow tables

Add hybrid attack mode (wordlist + mutations)

GUI interface
