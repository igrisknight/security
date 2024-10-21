# Function to encrypt the plaintext using Transposition Cipher
def transposition_encrypt(plaintext, key):
    # Remove any spaces from the plaintext and initialize the ciphertext
    plaintext = plaintext.replace(" ", "")
    ciphertext = [''] * key
    
    # Fill the columns for the transposition cipher
    for col in range(key):
        pointer = col
        # Loop through each column
        while pointer < len(plaintext):
            # Place the character in the respective column
            ciphertext[col] += plaintext[pointer]
            # Move pointer to the next character in the same column
            pointer += key
    
    # Combine the columns to form the final ciphertext
    return ''.join(ciphertext)

# Function to decrypt the ciphertext using Transposition Cipher
def transposition_decrypt(ciphertext, key):
    # Calculate the number of columns and rows needed for the grid
    num_cols = key
    num_rows = len(ciphertext) // key
    num_shaded_boxes = len(ciphertext) % key

    # Create an empty list to store the decrypted plaintext
    plaintext = [''] * num_cols

    # Variables to track the position in the grid
    col = 0
    row = 0

    # Calculate how many characters should be in each column
    col_lengths = [num_rows + 1 if col < num_shaded_boxes else num_rows for col in range(num_cols)]

    # Create an index to track the current position in ciphertext
    index = 0

    # Fill the grid with characters from the ciphertext
    for col in range(num_cols):
        current_col_length = col_lengths[col]
        plaintext[col] = ciphertext[index:index + current_col_length]
        index += current_col_length

    # Now read the grid row by row to reconstruct the plaintext
    decrypted_text = []
    for row in range(num_rows + 1):
        for col in range(num_cols):
            if row < len(plaintext[col]):
                decrypted_text.append(plaintext[col][row])

    return ''.join(decrypted_text)

# Example usage
plaintext = "THIS IS A TRANSPOSITION CIPHER"
key = 6

# Encrypting the plaintext
ciphertext = transposition_encrypt(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")

# Decrypting the ciphertext
decrypted_text = transposition_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
