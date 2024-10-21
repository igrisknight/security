# Function to generate the matrix for the Playfair Cipher
def generate_matrix(key):
    key = key.upper().replace('J', 'I')  # Replace J with I
    matrix = []
    used = set()

    # Add characters from the key to the matrix
    for char in key:
        if char not in used and char.isalpha():
            matrix.append(char)
            used.add(char)

    # Add the remaining characters (A-Z except J) to the matrix
    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in used:
            matrix.append(char)
            used.add(char)

    # Reshape the list into a 5x5 matrix
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

# Function to format the plaintext
def format_plaintext(plaintext):
    plaintext = plaintext.upper().replace('J', 'I')
    formatted_text = ''

    i = 0
    while i < len(plaintext):
        formatted_text += plaintext[i]
        # Check for repeating characters
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            formatted_text += 'X'  # Insert X between repeating characters
        elif i + 1 >= len(plaintext):
            formatted_text += 'X'  # Add X if the text length is odd
        else:
            formatted_text += plaintext[i + 1]
        i += 2

    return formatted_text  # Correctly return formatted text

# Function to find the position of a character in the matrix
def find_position(char, matrix):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

# Function to apply the Playfair cipher rule for encryption
def encrypt_pair(a, b, matrix):
    row_a, col_a = find_position(a, matrix)
    row_b, col_b = find_position(b, matrix)

    # Case 1: If both characters are in the same row
    if row_a == row_b:
        return matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
    # Case 2: If both characters are in the same column
    elif col_a == col_b:
        return matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
    # Case 3: If the characters form a rectangle (swap columns)
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]

# Function to encrypt the plaintext using the Playfair Cipher
def encrypt(plaintext, key):
    # Generate the Playfair matrix based on the key
    matrix = generate_matrix(key)
    
    # Format the plaintext by pairing the letters
    formatted_text = format_plaintext(plaintext)

    encrypted_text = ""

    # Encrypt each pair of letters
    for i in range(0, len(formatted_text), 2):
        encrypted_text += encrypt_pair(formatted_text[i], formatted_text[i + 1], matrix)

    return encrypted_text

# Example usage:
key = "KEYWORD"
plaintext = "HELLO"

ciphertext = encrypt(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
