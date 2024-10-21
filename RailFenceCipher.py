# Function to encrypt using the Rail Fence Cipher
def rail_fence_encrypt(plaintext, key):
    # Create a matrix to store the zigzag pattern
    rail = [['\n' for i in range(len(plaintext))] for j in range(key)]
    
    # To determine the direction of movement (down or up the rail)
    direction_down = False
    row = 0

    # Populate the matrix with characters of the plaintext
    for i in range(len(plaintext)):
        # Place the character in the appropriate row
        rail[row][i] = plaintext[i]

        # Change direction if we reach the top or bottom rail
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        
        # Move to the next row (down or up)
        row = row + 1 if direction_down else row - 1

    # Retrieve the cipher text from the zigzag pattern
    cipher = []
    for i in range(key):
        for j in range(len(plaintext)):
            if rail[i][j] != '\n':
                cipher.append(rail[i][j])
    return "".join(cipher)

# Function to decrypt the Rail Fence Cipher
def rail_fence_decrypt(ciphertext, key):
    # Create a matrix to store the zigzag pattern
    rail = [['\n' for i in range(len(ciphertext))] for j in range(key)]

    # To determine the direction of movement (down or up the rail)
    direction_down = None
    row, index = 0, 0

    # Mark the places in the matrix where characters will be placed
    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        # Mark this cell with '*'
        rail[row][i] = '*'

        # Move to the next row (down or up)
        row = row + 1 if direction_down else row - 1

    # Now, place the ciphertext characters in the matrix following the zigzag pattern
    for i in range(key):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    # Read the matrix in a zigzag pattern to retrieve the original message
    result = []
    row, direction_down = 0, True
    for i in range(len(ciphertext)):
        # Append the character to the result
        result.append(rail[row][i])

        # Change direction if we reach the top or bottom rail
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False

        # Move to the next row (down or up)
        row = row + 1 if direction_down else row - 1

    return "".join(result)

# Example usage
plaintext = "HELLOFROMTHEOTHERWORLD"
key = 3

ciphertext = rail_fence_encrypt(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")

# Decrypting the cipher
decrypted_text = rail_fence_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
