def gcd(a, b):
    """Calculate the greatest common divisor of a and b."""
    if a == 0:
        return b
    return gcd(b % a, a)

def generateKeys(p, q):
    """Generate the public and private keys."""
    n = p * q
    totient = (p - 1) * (q - 1)
    
    # Generate public key
    public = None
    for i in range(2, totient):
        if gcd(i, totient) == 1:
            public = i
            break
    
    # Generate private key using the Extended Euclidean Algorithm
    private = None
    for k in range(1, 10):
        private = (1 + k * totient) // public
        if (private * public) % totient == 1:  # Check if private key is valid
            break

    return (public, private)

def encrypt(message, public, n):
    """Encrypt the message using the public key."""
    return (message ** public) % n

def decrypt(encrypted_message, private, n):
    """Decrypt the message using the private key."""
    return (encrypted_message ** private) % n

def main():
    p = int(input('Enter value of p (a prime number): '))
    q = int(input('Enter value of q (another prime number): '))
    
    # Calculate n
    n = p * q

    plaintext = int(input('Enter the message (integer): '))
    if plaintext >= n:
        print('Message too large')
        return
    
    e, d = generateKeys(p, q)
    encrypted = encrypt(plaintext, e, n)
    decrypted = decrypt(encrypted, d, n)  # Use private key for decryption
    
    print(f"Public key: {e}")
    print(f"Private key: {d}")
    print(f"Encrypted message: {encrypted}")
    print(f"Decrypted message: {decrypted}")

# Run the main function
main()
