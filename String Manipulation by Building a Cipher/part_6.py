#Step 72: Modify the vigenere function so that its direction parameter has a default value of 1.
def vigenere(message, key, direction=1):

#Step 73: Now you can remove the third argument from your first function call.
encryption = vigenere(text, custom_key)

#Step 74: Right now, punctuation, special characters or digits are not encoded/decoded correctly.
# Check this by adding an exclamation mark at the end of the text string.
text = 'Hello Zaira!'
custom_key = 'python'

#Step 75: Modify the if condition by calling .isalpha() on char.
if char.isalpha():
    final_message += char

#Step 76: Add the not operator to the if condition to check if the character is not alphabetic.
if not char.isalpha():

#Step 77: Modify your comment into Append any non-letter character to the message.
#Step 78: Create a new function called encrypt that takes message and key parameters, and use pass to fill the function body.
def encrypt(message, key):
    pass

#Step 79: From your new function, return vigenere(message, key).
    return vigenere(message, key)

#Step 80: Define another function called decrypt with the same parameters. This time return vigenere(message, key, -1).
def decrypt(message, key):
    return vigenere(message, key, -1)

#Step 81: Next, modify your encryption and decryption variables by calling encrypt and decrypt, respectively.
def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)
    
encryption = encrypt(text, custom_key)
print(encryption)
decryption = decrypt(encryption, custom_key)
print(decryption)

#Note: I was stuck on this for a while as I had -1 in my decrypt call which was causing the code to be stuck on the step.

#Step 82: Change your text variable into mrttaqrhknsw ih puggrur.
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'

#Step 83: Modify print(encryption) to print Encrypted text: mrttaqrhknsw ih puggrur. Use the + operator to concatenate text to your string and pay attention to the spacing.
encryption = encrypt(text, custom_key)
print('Encrypted text: ' + text)

#Step 84: add another print() call to print Key: python. Again, use concatenation (+) to get this result.
print('Key: ' + custom_key)
decryption = decrypt(encryption, custom_key)
print(decryption)

#Step 85: Modify your last print() call to print Decrypted text: + decryption.
decryption = decrypt(encryption, custom_key)
print('Decrypted text: ' + decryption)

#Step 86: Delete encryption and pass text as the first argument to decrypt.
print('Encrypted text: ' + text)
print('Key: ' + custom_key)
decryption = decrypt(text, custom_key)
print('Decrypted text: ' + decryption)

#Step 87: You need to put an f before the quotes to create the f-string and write the variables or expressions you want to interpolate between curly braces.

# Modify the first print() call to use an f-string.
print(f'Encrypted text: {text}')

#Step 88: modify the other two print() calls to use f-strings.
print(f'Encrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'Decrypted text: {decryption}')

#Step 89: Put a newline character at the beginning of your first print call and see the output.
print(f'\nEncrypted text: {text}')

#Step 90:Add two newline characters to your last print() call: one at the beginning and the other one at the end of the string.
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')

#Step 91: You cannot decrypt anything with the wrong key. Try with happycoding. With that, your cipher project is complete.
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')

#Note: remember to find the index of text & custom key to encrypt/decrypt