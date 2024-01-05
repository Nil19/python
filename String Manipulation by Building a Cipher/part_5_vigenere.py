#Step 52
#currently, every single letter is always encrypted with the same letter, depending on the specified offset. 
#What if the offset were different for each letter? That would be much more difficult to decrypt. 
#This algorithm is referred to as the Vigenère cipher, where the offset for each letter is determined by another text, called the key.

#Step 53: modify your function declaration: change the function name into vigenere and the second parameter into key.
text = 'Hello Zaira'
shift = 3

def vigenere(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

#step 54: Delete your shift variable. Then, declare a new variable called custom_key and assign the value of the string python to this variable.
text = 'Hello Zaira'
custom_key = 'python'

#Step 55: At the beginning of your function body, declare a key_index variable and set it to zero.

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

#step 56: Before your if statement, add a comment saying Append space to the message.
 #Append space to the message
if char == ' ':
    encrypted_text += char
