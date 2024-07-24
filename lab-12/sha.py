import hashlib


def calculate_sha256(input_string):
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
    return sha256_hash


user_input = input("Enter a string to calculate its SHA-256 hash: ")
sha256_result = calculate_sha256(user_input)
print(f"SHA-256 Hash: {sha256_result}")