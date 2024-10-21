import math

def getPermutation(key):
    """Get the permutation order based on the sorted key."""
    sorted_key = sorted(list(enumerate(key)), key=lambda x: x[1])
    permutation = [_[0] for _ in sorted_key]
    return permutation

def encrypt(plaintext, key):
    """Encrypt the plaintext using the columnar transposition cipher."""
    ciphertext = ''
    permutation = getPermutation(key)
    
    # Calculate the number of rows needed for the plaintext
    rows = math.ceil(len(plaintext) / len(key))
    cols = len(key)

    # Create a matrix to hold the characters
    matrix = [['_' for _ in range(cols)] for _ in range(rows)]

    index = 0
    # Fill the matrix with the plaintext
    for i in range(rows):
        for j in range(cols):
            if index < len(plaintext):
                matrix[i][j] = plaintext[index]
                index += 1

    # Read columns according to the permutation order
    for num in permutation:
        for i in range(rows):
            ciphertext += matrix[i][num]

    return ciphertext

def decrypt(ciphertext, key):
    """Decrypt the ciphertext using the columnar transposition cipher."""
    rows = math.ceil(len(ciphertext) / len(key))
    cols = len(key)
    
    # Create a matrix to hold the characters
    matrix = [['_' for _ in range(cols)] for _ in range(rows)]
    
    # Get the permutation of the key
    permutation = getPermutation(key)

    # Fill the matrix in the order of the permutation
    index = 0
    for col in sorted(range(len(key)), key=lambda x: permutation[x]):
        for row in range(rows):
            if index < len(ciphertext):
                matrix[row][col] = ciphertext[index]
                index += 1

    # Read the matrix row-wise to get the plaintext
    plaintext = ''
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != '_':
                plaintext += matrix[i][j]

    return plaintext

# Main execution
text = input('Enter message: ')
key = input('Enter key: ')
e = encrypt(text, key)
d = decrypt(e, key)
print(f'Encrypted: {e}')
print(f'Decrypted: {d}')
