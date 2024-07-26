def gcd(a, b):
    if a == 0:
        return b
 
    return gcd(b % a, a)
 
 
print("gcd(", 10, ",", 15, ") = ", gcd(10, 15))
print("gcd(", 35, ",", 10, ") = ", gcd(35, 10))
print("gcd(", 31, ",", 2, ") = ", gcd(31, 2))
