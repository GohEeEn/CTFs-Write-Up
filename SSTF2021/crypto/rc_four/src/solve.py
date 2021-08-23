#!/usr/bin/env python3

from binascii import unhexlify


ct1, ct2 = open("output.txt").read().strip().split("\n")
msg = b"RC4 is a Stream Cipher, which is very simple and fast."

ct1 = unhexlify(ct1)
ct2 = unhexlify(ct2)

l = min(len(ct1), len(ct2))
r = ""

counter = 0

for (c1, m, c2) in zip(ct1[:l], msg[:l], ct2[:l]):
	r += chr((c1 ^ m) ^ c2)

print(r)