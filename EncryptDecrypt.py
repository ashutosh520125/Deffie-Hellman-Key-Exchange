
import os
from Crypto.Cipher import AES
def encrypt_message(u,key,f,y):
    file = open(f,"rb")
    message=file.read()
    file.close()

    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext,tag= cipher.encrypt_and_digest(message)

    path=os.path.join(u,y)
    file1=open(os.path.join(path,"out.txt"),"wb")
    file2=open(os.path.join(path,"n.txt"),"wb")
    file2.write(nonce)
    file1.write(ciphertext)
    file1.close()
    file2.close()

def decrypt_message(u,key,f,y):
    file = open(f,"rb")
    ciphertext=file.read()
    file.close()
    path=os.path.join(u,y)
    file1=open(os.path.join(path,"n.txt"),"rb")
    nonce=file1.read()
    file1.close()
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext