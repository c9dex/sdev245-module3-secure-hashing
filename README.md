# SDEV245 Module 3: Secure Hashing and Encryption

## Project Description

This Python project demonstrates three basic cryptography concepts: SHA-256 hashing, Caesar cipher encryption and decryption, and digital signatures.

## Features

### 1. SHA-256 Hashing
The program uses Python's `hashlib` library to generate SHA-256 hashes for user-entered messages and a sample text file named `test.txt`.

SHA-256 produces a 256-bit hash that can be used to check data integrity.

### 2. Caesar Cipher
The program encrypts messages by shifting letters through the alphabet using a number entered by the user.

It also decrypts the message by reversing the shift.

For example:
- Original: HELLO
- Shift: 3
- Encrypted: KHOOR
- Decrypted: HELLO

The Caesar cipher is for educational purposes and is not secure for modern applications.

### 3. Digital Signatures
The program uses Python's `cryptography` library to generate an RSA private/public key pair.

The private key signs a message, and the public key verifies the signature.

The program also changes the signed message to demonstrate that signature verification fails when the data has been modified.

## Requirements

- Python 3
- Python `cryptography` library

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Install the required library using `python -m pip install cryptography`.
4. Run the program using `python main.py`.
5. Follow the prompts to test hashing, encryption, decryption, and digital signatures.

Keep `test.txt` in the same folder as `main.py`.

## Learning Outcomes

This project helped me understand how hashing can verify data integrity, how substitution ciphers work, and how private and public keys are used for digital signatures.

## References

Python Caesar Cipher Tutorial:
https://www.youtube.com/watch?v=x71kJyNvB5o

OpenSSL Cryptography Basics:
https://opensource.com/article/19/6/cryptography-basics-openssl-part-2