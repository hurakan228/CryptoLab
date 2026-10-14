
import os
import streamlit as st
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.exceptions import InvalidTag
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError

st.set_page_config(
    page_title="CryptoLab",
    page_icon="🔐",
    layout="centered"
)

MAGIC = b"CLAB1"
ITERATIONS = 600_000
ph = PasswordHasher()


def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS
    )
    return kdf.derive(password.encode("utf-8"))


def encrypt_file(data, password):
    salt = os.urandom(16)
    nonce = os.urandom(12)
    key = derive_key(password, salt)

    aes = AESGCM(key)
    encrypted = aes.encrypt(nonce, data, None)

    return MAGIC + salt + nonce + encrypted


def decrypt_file(data, password):
    if len(data) < 49 or not data.startswith(MAGIC):
        raise ValueError("Invalid encrypted file")

    salt = data[5:21]
    nonce = data[21:33]
    encrypted = data[33:]

    key = derive_key(password, salt)
    aes = AESGCM(key)

    return aes.decrypt(nonce, encrypted, None)


st.title("🔐 CryptoLab")
st.write(" Lab #5 — Cryptography Application")
st.divider()

tab1, tab2, tab3 = st.tabs([
    "🔒 Encrypt",
    "🔓 Decrypt",
    "🔑 Password Hashing"
])

with tab1:
    st.header("File Encryption")
    st.write("Encrypt your files using AES-256-GCM.")

    file = st.file_uploader(
        "Choose a file",
        key="encrypt_file"
    )
    password = st.text_input(
        "Encryption password",
        type="password",
        key="encrypt_password"
    )

    if st.button("Encrypt File"):
        if file is None or not password:
            st.warning("Please select a file and enter a password.")
        else:
            encrypted = encrypt_file(file.getvalue(), password)
            st.success("File encrypted successfully!")

            st.download_button(
                "Download Encrypted File",
                data=encrypted,
                file_name=file.name + ".enc",
                mime="application/octet-stream"
            )

with tab2:
    st.header("File Decryption")
    st.write("Decrypt a file using the correct password.")

    encrypted_file = st.file_uploader(
        "Choose encrypted file",
        key="decrypt_file"
    )
    decrypt_password = st.text_input(
        "Decryption password",
        type="password",
        key="decrypt_password"
    )

    if st.button("Decrypt File"):
        if encrypted_file is None or not decrypt_password:
            st.warning("Please select a file and enter a password.")
        else:
            try:
                decrypted = decrypt_file(
                    encrypted_file.getvalue(),
                    decrypt_password
                )

                st.success("File decrypted successfully!")

                output_name = encrypted_file.name
                if output_name.endswith(".enc"):
                    output_name = output_name[:-4]
                else:
                    output_name = "decrypted_file"

                st.download_button(
                    "Download Decrypted File",
                    data=decrypted,
                    file_name=output_name,
                    mime="application/octet-stream"
                )

            except (InvalidTag, ValueError):
                st.error("Wrong password or invalid encrypted file.")

with tab3:
    st.header("Password Hashing")
    st.write("Secure password hashing using Argon2id.")

    password_to_hash = st.text_input(
        "Enter password to hash",
        type="password",
        key="hash_password"
    )

    if st.button("Generate Hash"):
        if not password_to_hash:
            st.warning("Enter a password first.")
        else:
            generated_hash = ph.hash(password_to_hash)
            st.session_state["generated_hash"] = generated_hash

    if "generated_hash" in st.session_state:
        st.success("Password hashed successfully!")
        st.code(st.session_state["generated_hash"])

    st.divider()
    st.subheader("Verify Password")

    saved_hash = st.text_area("Enter stored hash")
    check_password = st.text_input(
        "Enter password to verify",
        type="password",
        key="verify_password"
    )

    if st.button("Verify Password"):
        if not saved_hash or not check_password:
            st.warning("Please fill in both fields.")
        else:
            try:
                ph.verify(saved_hash.strip(), check_password)
                st.success("Password is correct!")
            except VerifyMismatchError:
                st.error("Incorrect password!")
            except (VerificationError, ValueError):
                st.error("Invalid hash format.")

st.divider()
st.caption("CryptoLab | Software Security and Secure Development")
