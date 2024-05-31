"""
Use `pip install sympy` to install prerequisite library
"""
from sympy import Matrix


def matrix_mod_inverse(matrix, mod):
    return Matrix(matrix).inv_mod(mod).tolist()


def text_to_matrix(text, n):
    text = text.replace(" ", "").upper()
    while len(text) % n != 0:
        text += 'X'
    return [[ord(char) - 65 for char in text[i:i + n]] for i in range(0, len(text), n)]


def matrix_multiply_mod(A, B, mod):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % mod for j in range(len(B[0]))] for i in range(len(A))]


def matrix_to_text(matrix):
    return ''.join(chr(num + 65) for row in matrix for num in row)


def hill_cipher_encrypt_decrypt(plaintext, key_matrix, mode='encrypt'):
    matrix_size = len(key_matrix)
    text_matrix = text_to_matrix(plaintext, matrix_size)
    text_matrix = [list(i) for i in zip(*text_matrix)]
    
    if mode == 'encrypt':
        result_matrix = matrix_multiply_mod(key_matrix, text_matrix, 26)
    else:
        key_matrix_inv = matrix_mod_inverse(key_matrix, 26)
        result_matrix = matrix_multiply_mod(key_matrix_inv, text_matrix, 26)
    
    result_matrix = [list(i) for i in zip(*result_matrix)]
    return matrix_to_text(result_matrix)


key_matrix = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]

plaintext = input("Enter plaintext: ").upper()

# Encryption
encrypted_text = hill_cipher_encrypt_decrypt(plaintext, key_matrix, mode='encrypt')
print("Encrypted Text:")
print(encrypted_text)

# Decryption
decrypted_text = hill_cipher_encrypt_decrypt(encrypted_text, key_matrix, mode='decrypt')
print("Decrypted Text:")
print(decrypted_text)
