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

#step 38: At the top of your for loop, replace print(char == ' ') with an if statement. 
# The condition of this if statement should evaluate to True if char is an empty space and False otherwise. 
# Inside the if body, print the string space!. Remember to indent this line.
for char in text.lower():
    if char == ' ':
        print('space!')

#step 39: Now, instead of printing space!, use the addition assignment operator to add the space to the current value of encrypted_text.
for char in text.lower():
    if char == ' ':
        encrypted_text += char 

#step 40: When the loop iterations reach the space, a space is added to the encrypted string. 
# To fix it, add an else clause after encrypted_text += char and indent all the subsequent lines of code.
for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = index + shift
        encrypted_text += alphabet[new_index]
        print('char:', char, 'encrypted text:', encrypted_text)

#Step 41: Try to assign the string Hello Zaira to your text variable and see what happens in the console. 
#output:
#char: h encrypted text: k
#char: e encrypted text: kh
#char: l encrypted text: kho
#char: l encrypted text: khoo
#char: o encrypted text: khoor

#Step 42: Surround index + shift with parentheses, and modulo the expression with 26, which is the alphabet length.
text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) %26
        encrypted_text += alphabet[new_index]

#step 43: If you wish to incorporate additional characters into the alphabet string, such as digits or special characters, you'll find it's necessary to manually 
#modify the right operand of the modulo operation. Replace 26 with len(alphabet) to avoid this issue.
else:
    index = alphabet.find(char)
    new_index = (index + shift) % len(alphabet)
    encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)

#Step 44: modify your print() call to print the encrypted message only and put it outside the for loop, so that the encrypted string is printed one time.
text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % len(alphabet)
        encrypted_text += alphabet[new_index]

print('encrypted text:', encrypted_text)
#output: encrypted text: khoor cdlud

#Step 45: Right before the print call, add another one to print 'plain text:', text. Use the same indentation.
print('plain text:', text)
print('encrypted text:', encrypted_text)
#output: 
#plain text: Hello Zaira
#encrypted text: khoor cdlud