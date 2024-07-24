import pyotp

# Generate a random key (this should be stored securely, usually per user; used as an identifier for TOTP)
user_id = pyotp.random_base32()  # or choose any user identifier as you wish

# Create a TOTP instance
totp = pyotp.TOTP(user_id)

# Generate the OTP
otp = totp.now()

print("User ID:", user_id)
print("Generated OTP:", otp)

# Simulate the user inputting the OTP
user_input_otp = input("Enter the OTP: ")

# Verify the OTP
is_valid_otp = totp.verify(user_input_otp)

if is_valid_otp:
    print("OTP is valid.")
else:
    print("OTP is not valid.")