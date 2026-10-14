# CryptoLab - Cybersecurity Lab #5

## Project Description

CryptoLab is a Python-based cryptography application developed for Cybersecurity Lab #5.

The application demonstrates two real-world cryptography use cases:

1. Secure file encryption using AES-256-GCM.
2. Secure password hashing using Argon2id.

## Technologies

- Python 3
- Streamlit
- Cryptography
- Argon2-cffi

## Feature 1: File Encryption

Algorithm: AES-256-GCM

AES-256-GCM provides confidentiality and integrity protection.

The application:
1. Accepts a file and password.
2. Generates a random 16-byte salt.
3. Derives a 256-bit key using PBKDF2-HMAC-SHA256 with 600,000 iterations.
4. Generates a random 12-byte nonce.
5. Encrypts the file using AES-256-GCM.
6. Allows decryption with the correct password.

Real-world use case: Protecting confidential documents.

## Feature 2: Password Hashing

Algorithm: Argon2id

Argon2id is a password-hashing algorithm designed to resist password-cracking attacks.

The application:
1. Accepts a password.
2. Generates a salted Argon2id hash.
3. Allows users to verify a password against the hash.

Real-world use case: Secure authentication systems.

## Installation

Create a virtual environment:

    python -m venv .venv

Install dependencies:

    .venv\Scripts\python.exe -m pip install -r requirements.txt

Run the application:

    .venv\Scripts\python.exe -m streamlit run app.py

Open:

    http://localhost:8501

## Testing
@'
# CryptoLab - Cybersecurity Lab #5

## Project Description

CryptoLab is a Python-based cryptography application developed for Cybersecurity Lab #5.

The application demonstrates two real-world cryptography use cases:

1. Secure file encryption using AES-256-GCM.
2. Secure password hashing using Argon2id.

## Technologies

- Python 3
- Streamlit
- Cryptography
- Argon2-cffi

## Feature 1: File Encryption

Algorithm: AES-256-GCM

AES-256-GCM provides confidentiality and integrity protection.

The application:
1. Accepts a file and password.
2. Generates a random 16-byte salt.
3. Derives a 256-bit key using PBKDF2-HMAC-SHA256 with 600,000 iterations.
4. Generates a random 12-byte nonce.
5. Encrypts the file using AES-256-GCM.
6. Allows decryption with the correct password.

Real-world use case: Protecting confidential documents.

## Feature 2: Password Hashing

Algorithm: Argon2id

Argon2id is a password-hashing algorithm designed to resist password-cracking attacks.

The application:
1. Accepts a password.
2. Generates a salted Argon2id hash.
3. Allows users to verify a password against the hash.

Real-world use case: Secure authentication systems.

## Installation

Create a virtual environment:

    python -m venv .venv

Install dependencies:

    .venv\Scripts\python.exe -m pip install -r requirements.txt

Run the application:

    .venv\Scripts\python.exe -m streamlit run app.py

Open:

    http://localhost:8501

## Testing

### AES-256-GCM

- File encryption: Successful
- Decryption using correct password: Successful
- Encrypted file cannot be read as plaintext

### Argon2id

- Password hash generation: Successful
- Correct password verification: Successful

## Open-Source Software Testing

Software: Cryptomator

Website: https://cryptomator.org/

Tests performed:
1. Created an encrypted vault.
2. Unlocked the vault using a password.
3. Added secret.txt to the encrypted vault.
4. Locked the vault.
5. Verified that protected files became inaccessible.
6. Unlocked the vault again to access the file.

Result: Successfully tested encrypted file storage.

## Security Notes

- AES-GCM detects tampering with encrypted data.
- Encryption passwords are not stored in the file.
- Argon2id hashes are not reversible encryption.
- Use strong, unique passwords.
- This is an educational demonstration, not an audited production system.

## Conclusion

CryptoLab demonstrates practical cryptographic mechanisms for protecting files and verifying passwords.

The project also includes testing of Cryptomator, an open-source encryption application.
