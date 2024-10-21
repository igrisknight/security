def getAlpha(q):
    """Find a primitive root (alpha) modulo q."""
    for alpha in range(2, q):  # Start from 2, as 1 is not a valid primitive root
        values = set()
        for i in range(1, q):
            value = pow(alpha, i, q)  # Calculate alpha^i mod q
            values.add(value)
        
        if len(values) == q - 1:  # If we get all values from 1 to q-1, alpha is valid
            return alpha

    return None  # If no primitive root is found

def generatePrivate(public, alpha, q):
    """Generate private key based on public key, alpha, and q."""
    return pow(alpha, public, q)  # Calculate alpha^public mod q

def generateKey(private, public, q):
    """Generate shared key using private key and other party's public key."""
    return pow(public, private, q)  # Calculate public^private mod q

def main():
    q = int(input('Enter value of q (a prime number): '))

    alpha = getAlpha(q)
    print(f'Primitive root (alpha): {alpha}')
    
    aPublic = int(input('Enter public key of A: '))
    bPublic = int(input('Enter public key of B: '))
    
    if aPublic >= q or bPublic >= q:
        print('Public key too large')
        exit()
    
    aPrivate = generatePrivate(aPublic, alpha, q)
    bPrivate = generatePrivate(bPublic, alpha, q)
    print(f'A: (Public: {aPublic}, Private: {aPrivate})')
    print(f'B: (Public: {bPublic}, Private: {bPrivate})')

    aKey = generateKey(aPrivate, bPublic, q)  # A computes the shared key
    bKey = generateKey(bPrivate, aPublic, q)  # B computes the shared key
    print(f'A shared key: {aKey}')
    print(f'B shared key: {bKey}')

if __name__ == "__main__":
    main()
