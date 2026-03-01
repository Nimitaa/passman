#!/usr/bin/env python3

import os
import json
import base64
import getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from colorama import Fore, Style, init

init(autoreset=True)

VAULT_FILE = "vault.dat"
SALT_FILE = "salt.bin"


# =========================
# Key Derivation
# =========================
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


# =========================
# Vault Loading
# =========================
def load_vault(master_password: str):
    if not os.path.exists(SALT_FILE):
        salt = os.urandom(16)
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
    else:
        with open(SALT_FILE, "rb") as f:
            salt = f.read()

    key = derive_key(master_password, salt)
    cipher = Fernet(key)

    if not os.path.exists(VAULT_FILE):
        return {}, cipher

    with open(VAULT_FILE, "rb") as f:
        encrypted_data = f.read()

    try:
        decrypted = cipher.decrypt(encrypted_data)
        return json.loads(decrypted.decode()), cipher
    except Exception:
        print(Fore.RED + "❌ Incorrect master password.")
        exit()


# =========================
# Save Vault
# =========================
def save_vault(data: dict, cipher: Fernet):
    encrypted = cipher.encrypt(json.dumps(data).encode())
    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted)


# =========================
# Re-Authentication
# =========================
def verify_master(master_password):
    check = getpass.getpass("Re-enter master password: ")
    if check != master_password:
        print(Fore.RED + "❌ Authentication failed.")
        return False
    return True


# =========================
# Features
# =========================
def add_entry(data):
    site = input("Site: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    data[site] = {"username": username, "password": password}
    print(Fore.GREEN + "✅ Entry added.")


def retrieve_entry(data):
    site = input("Site to retrieve: ")

    if site in data:
        print("Username:", data[site]["username"])
        show = input("Show password? (y/n): ").lower()

        if show == "y":
            print("Password:", data[site]["password"])
        else:
            print("Password: ********")
    else:
        print(Fore.RED + "❌ Not found.")


def delete_entry(data):
    site = input("Site to delete: ")

    if site in data:
        del data[site]
        print(Fore.YELLOW + "🗑 Entry deleted.")
    else:
        print(Fore.RED + "❌ Not found.")


def search_entries(data):
    term = input("Search term: ").lower()
    found = False

    for site in data:
        if term in site.lower():
            print("-", site)
            found = True

    if not found:
        print(Fore.RED + "❌ No matches found.")


# =========================
# Main
# =========================
def main():

    print(Fore.BLUE +
r"""
██████╗  █████╗ ███████╗███████╗███╗   ███╗ █████╗ ███╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝████╗ ████║██╔══██╗████╗  ██║
██████╔╝███████║███████╗███████╗██╔████╔██║███████║██╔██╗ ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║     ██║  ██║███████║███████║██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
        🔐  Encrypted Local Password Manager  🔐
""" + Style.RESET_ALL)

    master_password = getpass.getpass("Enter master password: ")

    data, cipher = load_vault(master_password)

    while True:
        print("\n1. Add")
        print("2. Retrieve")
        print("3. Delete (Protected)")
        print("4. Search")
        print("5. Exit")

        choice = input("Select: ")

        if choice == "1":
            add_entry(data)
            save_vault(data, cipher)

        elif choice == "2":
            retrieve_entry(data)

        elif choice == "3":
            if verify_master(master_password):
                delete_entry(data)
                save_vault(data, cipher)

        elif choice == "4":
            search_entries(data)

        elif choice == "5":
            print(Fore.MAGENTA + "Goodbye.")
            break

        else:
            print(Fore.RED + "Invalid option.")


if __name__ == "__main__":
    main()
