from cryptography.fernet import Fernet


def encryption(org_txt):
    cipher_key = Fernet.generate_key()
    org_txt=org_txt.encode('utf-8')
    cipher = Fernet(cipher_key)
    encrypted_text = cipher.encrypt(org_txt)
    Final_txt=encrypted_text.decode("utf-8")
    cipherKey=cipher_key.decode("utf-8")

    return Final_txt,cipherKey
    
def dec(or_txt,key):
     or_txt=or_txt.encode("utf-8")
     key=key.encode("utf-8")
     cipher2= Fernet(key)
     dcr_txt = cipher2.decrypt(or_txt)
     decrypted_text = dcr_txt.decode("utf-8")
     return decrypted_text

def inpu():
    a=input("enter the text")
    b=input("press 1 to do Encryption and 2 For Decryption")
    if(b=='1'):
         res=encryption(a,cipher_key)
         print("Your key is "+str(cipherKey))
         print("Text is : " + str(res))
         dec(res,cipherKey)
    elif(b=='2'):
        c=input("Enter 2 to decrypt the text")
        if(c==2):
            d=input("Enter the Encrypted text now ")
            e=input("Enter the key")
            dec(d,e)
        
    else:
        print("wrong choice")
    
        