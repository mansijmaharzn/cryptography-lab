def galois_mult(a, b):
    """Galois Field (256) Multiplication of two Bytes"""
    p = 0
    hi_bit_set = 0
    for i in range(8):
        if (b & 1) == 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set == 0x80:
            a ^= 0x1b  # XOR with the irreducible polynomial
        b >>= 1
    return p % 256

def mix_single_column(column):
    """Perform the MixColumns step on a single column"""
    temp = column.copy()
    column[0] = galois_mult(temp[0], 2) ^ galois_mult(temp[1], 3) ^ temp[2] ^ temp[3]
    column[1] = temp[0] ^ galois_mult(temp[1], 2) ^ galois_mult(temp[2], 3) ^ temp[3]
    column[2] = temp[0] ^ temp[1] ^ galois_mult(temp[2], 2) ^ galois_mult(temp[3], 3)
    column[3] = galois_mult(temp[0], 3) ^ temp[1] ^ temp[2] ^ galois_mult(temp[3], 2)

def mix_columns(state):
    """Perform the MixColumns step on the state"""
    for i in range(4):
        mix_single_column(state[i])

# Example usage
state = [
    [0x87, 0xf2, 0x4d, 0x97],
    [0x6e, 0x4c, 0x90, 0xec],
    [0x46, 0xe7, 0x4a, 0xc3],
    [0xa6, 0x8c, 0xd8, 0x95]
]

print("Before MixColumns:")
for row in state:
    print([hex(x) for x in row])

mix_columns(state)

print("\nAfter MixColumns:")
for row in state:
    print([hex(x) for x in row])
