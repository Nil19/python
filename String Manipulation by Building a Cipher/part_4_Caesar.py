#Step 46: Right after your shift variable, declare a function called caesar and indent the following lines, so they become the function body.
text = 'Hello Zaira'
shift = 3
def caesar():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', text)
    print('encrypted text:', encrypted_text)

#Step 47: At the end of your code, call your caesar function. Pay attention to the indentation.
caesar()

#Step 48: Modify your function declaration so that it takes two parameters called message and offset.
def caesar(message, offset):

#step 48& 49 :Modify your function declaration so that it takes two parameters called message and offset. Inside your function body, 
#rename the text and shift variables to message and offset, respectively.
text = 'Hello Zaira'
shift = 3

def caesar(message, offset):
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

caesar()

#Step 50: Give message and offset values, by passing text and shift as arguments to the caesar function call.
caesar(text, shift)

#step 51: pass the text variable and the integer 13 as arguments.
caesar(text, 13)
