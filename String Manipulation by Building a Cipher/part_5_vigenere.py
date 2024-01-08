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

#Step 57: Inside the else block, declare a variable called key_char and assign it the value of key at the index key_index mod(%) the length of key.
    if char == ' ':
        encrypted_text += char
    else:
        key_char = key[key_index % len(key)]

#Step 58: increase the key_index count for the next iteration. To do this, after the line you just added and in the same code block, 
#use the addition assignment operator to increment key_index by one.
    else:
        key_char = key[key_index % len(key)]
        key_index += 1

#Step 59: Inside the else clause, write a comment saying Find the right key character to encode.

#Step 60: Declare a variable called offset and give it the value of the ind
    else:        
    # Find the right key character to encode
        key_char = key[key_index % len(key)]
        key_index += 1
        offset = alphabet.index(key_char)

#Step 61: Create another comment saying Define the offset and the encrypted letter.
#Step 62: Remove the two print() calls from your function and return encrypted_text.
# Define the offset and the encrypted letter
        offset = alphabet.index(key_char)
        index = alphabet.find(char)
        new_index = (index + offset) % len(alphabet)
        encrypted_text += alphabet[new_index]
    return encrypted_text

# Step 63: Call your function passing text and custom_key as the arguments. Store the return value of the function call in a variable called encryption.
encryption = vigenere(text,custom_key)

# Step 64: And now, try to print encryption to see the actual output on the terminal.
print(encryption)

#Step 65: Add a third parameter called direction to your function definition. Also, comment out the last two lines to avoid errors in the console.
text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key, direction):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
    
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:        
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text
#encryption = vigenere(text, custom_key)
#print(encryption)

#Step 66: All you need to do is multiply the offset by the direction in the new_index assignment. The multiplication operator in Python is *.
new_index = (index + offset * direction) % len(alphabet)

#Step 67: uncomment the last two lines and modify your function call passing 1 as the third argument.
encryption = vigenere(text, custom_key, 1)
print(encryption)

#output: wcesc mpgkh

#Step 68: Declare another variable called decryption and assign it vigenere(encryption, custom_key, -1).
decryption = vigenere(encryption, custom_key, -1)

#Step 69: Now print your decryption variable.
print(decryption)
#output: hello zaira

#Step 70: Clean up your code with better variable names.Change each occurrence of encrypted_text into final_message.
#Step 71: Update your comments too. Your first comment should say encode/decode and your second comment should say encrypted/decrypted.
text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key, direction):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
    
        # Append space to the message
        if char == ' ':
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
    
encryption = vigenere(text, custom_key, 1)
print(encryption)
decryption = vigenere(encryption, custom_key, -1)
print(decryption)
