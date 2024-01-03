#LOOPS

#step 18: Remove everything after the alphabet line. Then write a for loop to iterate over text.
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in text:

#step 19: Give your for loop a body by adding a call to print(i). Remember to indent the loop body
    print(i)

#output:
#>>> H
#>>> e
#>>> l
#>>> l
#>>> o
#>>>  
#>>> W
#>>> o
#>>> r
#>>> l
#>>> d   
    
#step 20 & 21: indentations, important to include indents when using loops.
    
#step 22: The iteration variable can have any valid name, but it's convenient to give it a meaningful name. Rename your i variable to char.
for char in text:
    print(char)

#step 23: Before printing the current character, declare a variable called index and assign the value returned by alphabet.find(char) to this variable.
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text:
    index = alphabet.find(char)
    print(char)

#step 24: Add a second argument to print(char) so that it prints the character and its index inside the alphabet.
    print(char , index)

#step 25: instead of iterating over text, change the for loop to iterate over text.lower().
for char in text.lower():
    index = alphabet.find(char)
    print(char, index)

#step 26: At the end of your loop body, declare a variable called new_index and assign the value of index + shift to this variable.
for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift

#output:
#>>> h 7
#>>> e 4
#>>> l 11
#>>> l 11
#>>> o 14
#>>>  -1 
#>>> w 22
#>>> o 14
#>>> r 17
#>>> l 11
#>>> d 3
    
#step 27: Use bracket notation to access the first letter in text and try to change it into a character of your choice.
text = 'Hello World'
text[0] = 'n'

#step 28: a variable can be reassigned another string. Delete the text[0] line and reassign text the string Albatross.
text = 'Hello World'
text = 'Albatross'

#step 29: n/a

#step 30: Now you need to create a new_char variable at the end of your loop body. Set its value to alphabet[new_index].
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift
    new_char = alphabet[new_index]

#output:
#>>> h 7
#>>> k
#>>> e 4
#>>> h
#>>> l 11
#>>> o
#>>> l 11
#>>> o
#>>> r
#>>> o 14
#>>>   -1
#>>> c
#>>> z
#>>> w 22
#>>> o 14
#>>> r
#>>> r 17
#>>> u
#>>> l 11
#>>> o
#>>> d 3
#>>> g

# note: 
# new_index = index + shift: Calculates the new index by adding the shift value.
# new_char = alphabet[new_index]: Retrieves the new character from the alphabet using the new index.
# print(new_char): Prints the encrypted character.
    
#step 31: Delete print(char, index), and turn the last print() call into print('char:', char, 'new char:', new_char).
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    new_char = alphabet[new_index]
    print('char:', char, 'new char:', new_char)

#output: 
# char: h new_char: k
# char: e new_char: h
# char: l new_char: o
# char: l new_char: o
# char: o new_char: r
# char:   new_char: c
# char: w new_char: z
# char: o new_char: r
# char: r new_char: u
# char: l new_char: o
# char: d new_char: g

