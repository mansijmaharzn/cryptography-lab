import hashlib
# Prompt user for input string
input_str = input("Enter string to encrypt using MD5: ")
# Encode the string as bytes
input_bytes = input_str.encode()
# Compute the MD5 hash of the input bytes
hash_object = hashlib.md5(input_bytes)
# Get the hexadecimal representation of the hash
hash_hex = hash_object.hexdigest()
# Print the result
print(f"MD5 hash of '{input_str}': {hash_hex}")