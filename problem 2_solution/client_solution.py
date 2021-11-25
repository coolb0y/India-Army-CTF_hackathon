import os
import pickle
# import required module
from cryptography.fernet import Fernet

def generate_key():
    # key generation
    key = Fernet.generate_key()
    # string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

def encrypt_file():

    
    generate_key()
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

    

def fun(name,password):
    s = {"username":name,"password":password}
    safecode = pickle.dumps(s)
    with open("users.json","wb") as f:
        f.write(safecode)
    return safecode

if __name__ == '__main__':
    u = input("Username : ")
    p = input("Password : ")
    yo_fun = fun(u,p)
    encrypt_file()