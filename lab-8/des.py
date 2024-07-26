from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode('utf-8'), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded_text = cipher.decrypt(ciphertext)
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    return decrypted_text.decode('utf-8')

# Generate a random 8-byte key (DES requires a key of exactly 8 bytes)
key = get_random_bytes(8)

# Example usage
plaintext = "This is a test message."
print(f"Plaintext: {plaintext}")

encrypted = des_encrypt(plaintext, key)
print(f"Encrypted: {encrypted}")

decrypted = des_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
