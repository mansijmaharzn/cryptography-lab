def prime_checker(p):
    if p < 2:
        return False
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False
    return True

def primitive_check(g, p):
    return len(set(pow(g, i, p) for i in range(1, p))) == p - 1

while True:
    P = int(input("Enter P (prime number): "))
    if prime_checker(P):
        break
    print("Number is not prime, please enter again!")

while True:
    G = int(input(f"Enter the primitive root of {P}: "))
    if primitive_check(G, P):
        break
    print(f"Number is not a primitive root of {P}, please try again!")

x1 = int(input("Enter the private key of User 1: "))
x2 = int(input("Enter the private key of User 2: "))
assert x1 < P and x2 < P, f"Private keys must be less than {P}!"

# Calculate Public Keys
y1, y2 = pow(G, x1, P), pow(G, x2, P)

# Generate Secret Keys
k1, k2 = pow(y2, x1, P), pow(y1, x2, P)

print(f"\nSecret Key for User 1 is {k1}\nSecret Key for User 2 is {k2}\n")
print("Keys have been exchanged successfully" if k1 == k2 else "Keys have not been exchanged successfully")
