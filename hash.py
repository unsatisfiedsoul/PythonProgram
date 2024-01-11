#!/bin/python3

import hashlib

def calculate_sha256(data):
	if isinstance(data,str):
		data = data.encode()

	sha256_hash = hashlib.sha256(data).hexdigest()
	return sha256_hash

input_data = input("What is your password: ")
hash_value = calculate_sha256(input_data)
print(hash_value)
