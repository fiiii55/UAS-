import rsa

def generate_keys():
    # Generate key pair
    (public_key, private_key) = rsa.newkeys(512)
    return public_key, private_key

def encrypt(plain_text, public_key):
    # Enkripsi menggunakan public key
    cipher_text = rsa.encrypt(plain_text.encode(), public_key)
    return cipher_text

def decrypt(cipher_text, private_key):
    # Dekripsi menggunakan private key
    plain_text = rsa.decrypt(cipher_text, private_key)
    return plain_text.decode()

# Contoh penggunaan
public_key, private_key = generate_keys()

plain_text = "Hello, World!"
cipher_text = encrypt(plain_text, public_key)
print("Cipher Text:", cipher_text)

decrypted_text = decrypt(cipher_text, private_key)
print("Decrypted Text:", decrypted_text)