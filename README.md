# passman
PassMan is a local encrypted password manager built in Python.
It  securely stores credentials encrypted on disk using AES-based symmetric encryption and a master password system 
--

## 🚀 Features

- Master password authentication
- AES encryption (via Fernet)
- PBKDF2 key derivation with SHA256
- Secure salt generation
- Encrypted JSON vault storage
- Add, Retrieve, Delete, Search entries
- Delete entries (Protected delete with re-authentication)
- Hidden password input
- Search stored entries

--
## 🔒 Security Design

- Encryption: AES (Fernet)
- Key Derivation: PBKDF2 (100,000 iterations)
- Salt: Random 16-byte salt stored separately
- No plaintext passwords stored on disk

sone credentails are('vault.dat')
---

## 📦 Installation

Clone the repository:
git clone https://github.com/Nimitaa/passman.git
cd passman
Create virtual environment:
sudo apt update
sudo apt install python3-venv 
python3 -m venv venv
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt (may take a lil time)
Run the program:
python passman.py

---
image /demo 
<img width="907" height="728" alt="Screenshot 2026-03-01 032804" src="https://github.com/user-attachments/assets/73c714e2-b825-4c3c-8dc8-e1c7c86bc371" />
and with password protection(with reauthentication)
<img width="966" height="333" alt="Screenshot 2026-03-01 033911" src="https://github.com/user-attachments/assets/a0884b8d-2fc3-4b6e-a27b-4ef053e2a90a" />

## 📁 Files

- passman.py → Main application
- vault.dat → Encrypted vault (created at runtime)
- salt.bin → Salt file (created at runtime)

---

## ⚠ Disclaimer

This project is for educational purposes.

git remote add origin https://github.com/Nimitaa/Syntexchub-internship.git
git branch -M main
git push -u origin main

