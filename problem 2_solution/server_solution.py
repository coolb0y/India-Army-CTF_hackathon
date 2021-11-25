import os
import pickle
from cryptography.fernet import Fernet


def encrypt_file():

  
    # opening the key
    with open('filekey.key', 'rb') as filekey:
	    key = filekey.read()

# using the generated key
    fernet = Fernet(key)

# opening the original file to encrypt
    with open('users.json', 'rb') as file:
	    original = file.read()

# encrypting the file
    encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
    with open('users.json', 'wb') as encrypted_file:
	    encrypted_file.write(encrypted)


def open_key():
    # key generation
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    return key

def decrypt_file():

    key = open_key()
    # using the key
    fernet = Fernet(key)

    # opening the encrypted file
    with open('users.json', 'rb') as enc_file:
    	encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
    # decrypted = fernet.decrypt(bytes(encrypted, 'utf-8'))

    # opening the file in write mode and
    # writing the decrypted data
    with open('users.json', 'wb') as dec_file:
    	dec_file.write(decrypted)


def reverse_fun():
    # decrypt_file()
    with open("users.json", "rb") as f:
        data = f.read()

    d = pickle.loads(data)
    # encrypt_file()

    return d


def helper():
    s = {"username": reverse_fun()['username'], "password": reverse_fun()['password']}
    safecode = pickle.dumps(s)
    with open("users.json", "wb") as f:
        f.write(safecode)
    return safecode

if __name__ == '__main__':
    decrypt_file()
    print(reverse_fun())
    helper()
    encrypt_file()
