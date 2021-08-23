#!/usr/bin/env python3

"""
Cryptohack - Passwords as Keys
Solution using the requests Python module
"""

import requests
import hashlib
from Crypto.Cipher import AES


BASE_URL = "http://aes.cryptohack.org/passwords_as_keys/"

# 1. Get the ciphertext of the encrypted flag
r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
ciphertext = data["ciphertext"]
print("ciphertext", ciphertext)

# 2. Brute-force the MD5 password hash
with open(words.txt) as f:
	for word in f:
		key = hashlib.md5(word.encode()).digest()
		cipher = AES.new(key, AWS.MODE_ECB)
		try:
			decrypted = cipher.decrypt(ciphertext)
		except ValueError as e:
			



# 2. Send the ciphertext to the decryption function
# r = requests.get(f"{BASE_URL}/decrypt/{ciphertext}/{password_hash}/")
# data = r.json()
# plaintext = data["plaintext"]
# print("plaintext", plaintext)

# 3. Convert the plaintext from hex to ASCII
# print("flag", bytearray.fromhex(plaintext).decode())