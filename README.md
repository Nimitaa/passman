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
python3 -m venv venv
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
Run the program:
python passman.py

---

## 📁 Files

- passman.py → Main application
- vault.dat → Encrypted vault (created at runtime)
- salt.bin → Salt file (created at runtime)

---

## ⚠ Disclaimer

This project is for educational purposes.


