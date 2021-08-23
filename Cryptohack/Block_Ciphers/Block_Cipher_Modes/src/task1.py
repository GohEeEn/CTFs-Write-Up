#!/usr/bin/env python3

"""
Cryptohack - Block Cipher Mode Starter
Solution using the requests Python module
"""

import requests

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter/"

# 1. Get the ciphertext of the encrypted flag
r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
ciphertext = data["ciphertext"]
print("ciphertext", ciphertext)

# 2. Send the ciphertext to the decryption function
r = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = r.json()
plaintext = data["plaintext"]
print("plaintext", plaintext)

# 3. Convert the plaintext from hex to ASCII
print("flag", bytearray.fromhex(plaintext).decode())