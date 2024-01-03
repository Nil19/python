#step 33: Before your for loop, declare a variable called encrypted_text and assign an empty string to this variable ('').
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''
for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    new_char = alphabet[new_index]
    print('char:', char, 'new char:', new_char)

#step 34: Now, replace new_char with encrypted_text. Also, modify the print() call to reflect this change.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''
for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text = alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)

#step 35: Instead of assigning alphabet[new_index] to encrypted_text, assign the current value of encrypted_text plus alphabet[new_index] to this variable
for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text = encrypted_text + alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)

#step 36: Use the addition assignment operator to add a value and assign it at the same time to encrypted_text.
encrypted_text += alphabet[new_index]

#step 37: At the top of your loop, print the result of comparing char with an empty space. Use the equality operator == for that.
for char in text.lower():
    print(char == ' ')
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)