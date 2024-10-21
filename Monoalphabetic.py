import string

# Function to initialize the cipher with the given key
def initialize_cipher(key):
    # Standard alphabets
    alphabets = string.ascii_lowercase

    # Check if the key is valid (length must be 26 and unique)
    if len(key) != 26 or len(set(key)) != 26:
        raise ValueError("Key must be a permutation of the 26 letters of the alphabet.")
    
    return alphabets, key.lower()

# Function to encrypt the plaintext using Monoalphabetic Cipher
def encrypt(plaintext, alphabets, key):
    ciphertext = []  # Prepare the ciphertext

    for char in plaintext:
        if char.isalpha():
            index = alphabets.index(char.lower())  # Get the index of the character in the alphabet
            cipher_char = key[index]  # Get the corresponding character from the key

            # Preserve the original case
            if char.isupper():
                cipher_char = cipher_char.upper()
            
            ciphertext.append(cipher_char)  # Append the encrypted character
        else:
            ciphertext.append(char)  # Non-alphabetic characters are appended unchanged

    return ''.join(ciphertext)

# Function to decrypt the ciphertext using monoalphabetic cipher
def decrypt(ciphertext, alphabets, key):
    plaintext = []  # Prepare to check the plaintext

    for char in ciphertext:
        if char.isalpha():
            index = key.index(char.lower())  # Get the index of the character from the key
            plain_char = alphabets[index]

            # Preserve the original case
            if char.isupper():
                plain_char = plain_char.upper()

            plaintext.append(plain_char)  # Append the decrypted character
        else:
            plaintext.append(char)  # Non-alphabetic characters are appended unchanged

    return ''.join(plaintext)

if __name__ == '__main__':
    key = "zyxwvutsrqponmlkjihgfedcba"  # Example substitution key
    alphabet, key = initialize_cipher(key)  # Initialize the cipher

    plaintext = input("Enter the plaintext: ")
    ciphertext = encrypt(plaintext, alphabet, key)
    print(f"Encrypted: {ciphertext}")

    decrypted_text = decrypt(ciphertext, alphabet, key)
    print(f"Decrypted: {decrypted_text}")
