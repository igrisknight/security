import string

#function to check the key len to initialize thw cipher
def initialize_cipher(text, key):

    # check the if the key is valid(length of key must be same as text unique)
    if len(key) != len(text):
        raise ValueError("Key must be the same length as the text")
    
    return key.upper()

# function to encrypt the plaintext using Vernam Cipher
def encrypt(plaintext, key):

    ciphertext = [] # prepare the ciphertext

    for char in range(len(plaintext)):
            cipher_char = (ord(plaintext[char]) - ord('A')) + (ord(key[char]) - ord('A')) # combining the ascii values from the plaintext 
            # and key to get substitution character

            # mainting the values within the 26 character limit
            if cipher_char >= 26:
                cipher_char -= 26
                
            ciphertext.append(chr(cipher_char + ord('A')))

    return ''.join(ciphertext)

# function to decrypt the ciphertext using vernam cipher
def decrypt(ciphertext, key):

    plaintext = [] # prepare the plaintext

    for char in range(len(ciphertext)):
            plain_char = (ord(ciphertext[char]) - ord('A')) - (ord(key[char]) - ord('A')) # combining the ascii values from the ciphertext 
            # and key to get substitution character

            # mainting the values within the 26 character limit
            if plain_char <= 0:
                plain_char += 26
                
            plaintext.append(chr(plain_char + ord('A')))

    return ''.join(plaintext)

message = input("enter the message: ") # message to be encrypt and decrypt
key = input("enter the keyword: ") # key used for the process

#intializing the key
initialize_cipher(message, key)

e = encrypt(message, key)
print(f"Encrypted: {e}")

d = decrypt(e, key)
print(f"Decrypted: {d}")



