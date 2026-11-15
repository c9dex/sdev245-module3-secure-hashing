
import hashlib

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Generate a SHA-256 hash from a message
def hash_message(message):
    encoded_message = message.encode("utf-8")
    hashed_message = hashlib.sha256(encoded_message)
    return hashed_message.hexdigest()


# Ask the user to enter a message
user_message = input("Enter a message to hash: ")

# Generate and display the hash
result = hash_message(user_message)

print("\nOriginal message:", user_message)
print("SHA-256 Hash:", result)

# Generate a SHA-256 hash from a file
def hash_file(filename):
    sha256 = hashlib.sha256()

    # Read the file in binary mode
    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


# Test hashing our sample file
print("\n--- File Hashing ---")
file_hash = hash_file("test.txt")
print("File: test.txt")
print("SHA-256 Hash:", file_hash)


# Caesar Cipher encryption and decryption
def caesar_cipher(message, shift):
    result = ""

    for char in message:
        if "A" <= char <= "Z":
            new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            result += new_char

        elif "a" <= char <= "z":
            new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            result += new_char

        else:
            result += char

    return result


# Ask the user for a message and shift
print("\n--- Caesar Cipher ---")
message = input("Enter a message to encrypt: ")
shift = int(input("Enter a shift number: "))

# Encrypt the message
encrypted = caesar_cipher(message, shift)
print("Encrypted message:", encrypted)

# Decrypt using the opposite shift
decrypted = caesar_cipher(encrypted, -shift)
print("Decrypted message:", decrypted)


# Digital Signature Simulation
def digital_signature_demo():
    print("\n--- Digital Signature Simulation ---")

    # Generate an RSA private and public key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    message = input("Enter a message to sign: ").encode("utf-8")

    # Sign the message with the private key
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("Message signed successfully!")

    # Verify the signature using the public key
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Signature verification: SUCCESS")
    except InvalidSignature:
        print("Signature verification: FAILED")





    # Test whether a modified message passes verification
    tampered_message = message + b" changed"

    try:
        public_key.verify(
            signature,
            tampered_message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Tampered message verification: SUCCESS")
    except InvalidSignature:
        print("Tampered message verification: FAILED (expected)")

# Run the digital signature demonstration
digital_signature_demo()