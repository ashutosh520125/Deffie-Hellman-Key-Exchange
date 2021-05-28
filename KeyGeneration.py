import hashlib
import binascii
import os

sharedPrime= 0xFFF0E86039B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81F56E880B96E71239B2FC81123213DC11
sharedBase = 2 

def generate_private_key(u):
    hex_key = binascii.b2a_hex(os.urandom(600))
    private_key = int(hex_key,16)
    public_key = pow(sharedBase,private_key,sharedPrime)
    file1=open(os.path.join(u,"private_key.txt"),"w")
    file2=open(os.path.join(u,"public_key.txt"),"w")
    file1.write(str(private_key))
    file2.write(str(public_key))
    file1.close()
    file2.close()
  
def generate_partial_key(u,x,y):
    path=os.path.join(u,x)
    file1 = open(os.path.join(path,"private_key.txt"), "r")
    x_private_key=file1.read()
    file1.close()

    path=os.path.join(u,y)
    file2 = open(os.path.join(path,"public_key.txt"), "r")
    y_public_key=file2.read()
    file2.close()

    x_private_key=int(x_private_key)
    y_public_key=int(y_public_key)

    full_key = pow(y_public_key,x_private_key,sharedPrime)
    return hashlib.sha256((str(full_key)).encode("utf-8")).digest()