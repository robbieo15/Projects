import string

def rot13encrypt():

    while True:

        listtoencrypt = (input("What are we trying to encrypt: "))

        #rotations = int(input("How many times would you like to rotate the cipher: "))
        code_keys = (string.ascii_lowercase+string.ascii_uppercase)
        code_values = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZabcdefghijklm'
        cipher = dict(zip(code_keys,code_values))
        decrypted_message = []
        encrypted_message = []

        for char in listtoencrypt:
            encrypted_message += cipher.get(char,char)
            decrypted_message += listtoencrypt
        
        print(encrypted_message)
        print(decrypted_message)
        


        print(f"This is your encrypted message {encrypted_message}")
        decrypt_question = int(input('Type any number > 0 to decrypt the message:')) 

        if decrypt_question > 0:
            print(f"This is your decrypted message: {decrypted_message} - look familiar?")
        
        tryagain = input("Type y if you want to try again: ").upper()
        if tryagain == 'Y':
            True
        else:
            False
            
rot13encrypt()
