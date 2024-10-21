#function to encrypt and decrypt messages.
def CeaserCipher(message, key, mode='encrypt'):
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #Convert the message to upper case to match the alphabets
    message = message.upper()

    #result variable to store the the final result
    result = ''

    #loop to encrypt and decrypt the message
    for letter in message:
        if letter in alphabets:
            index = alphabets.index(letter)

            #checking the mode to see if the messages needs to be encrypted or decrypted
            if mode == 'encrypt':
                #ceaser cipher encryption formula
                index = (index + key) % len(alphabets)
            elif mode == 'decrypt':
                #ceaser cipher decryption formula
                index = (index - key) % len(alphabets)

            result += alphabets[index]
        else:
            #Add any special characters without any chages
            result += letter
    
    return result

#example usage
message = input("enter the message: ")
key = 3

#encrypting the plain text
encryted_text = CeaserCipher(message, key, mode='encrypt')
print("encrypter message: ", encryted_text)

#decrypting the encrypted text
decrypted_text = CeaserCipher(message, key, mode='decrypt')
print("encrypter message: ", decrypted_text)

        
