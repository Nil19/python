#Step 1: Create a variable called number and assign it the value 5.
number = 5

#Step 2: Delete your number variable and its value. Then, declare another variable called text and assign the string Hello World to this variable. 
text = "Hello World"
#Step 3: Print it
print(text)

#output: Hello World

#Step 4: Now, instead of printing text, print just the character at index 6.
text = "Hello World"
print(text[6])

#output: W

#Step 5: modify your existing print() call to print the last character in your string.
text = 'Hello World'
print(text[-1])

#output: d

#Step 6: find the number of characters in a string with the built-in len() function.
text = 'Hello World'
print (len(text))

#output: 11

#Step 7: Another useful built-in function is type(), which returns the data type of a variable.
text = 'Hello World'
print(type(text))

#output: <class 'str'>

#Step 8: Now go to a new line and create another variable called shift and assign the value 3 to this variable.
text = 'Hello World'
print(type(text))

shift = 3
#Step 9: Print new line
print(shift)

#output: 
#<class 'str'>
# 3

#Step 10: Call the type() function and print the data type of your shift variable.
text = 'Hello World'
print(type(text))
shift = 3
print(type(shift))
#output: 
#class 'str'>
#<class 'int'>

#step 11: Remove both calls to print() and declare another variable called alphabet. Assign the string abcdefghijklmnopqrstuvwxyz to this variable.
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#step 12: At the end of your code, call find() on your alphabet string and pass text[0] to the function.
alphabet.find(text[0])

#step 13: Now assign the value returned by alphabet.find(text[0]) to a variable named index. Then, print its value.
index = alphabet.find(text[0])
print(index)

#step 14: Add another print() call to print text.lower() and see the output.
print (text.lower())
#output: hello world

#step 15: Remove the last print() call. Then, instead of text[0], pass text[0].lower() to find() and see the output.
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)

#output: 7
#note: The output should be 7 because the first character of the string text is 'H', and when converted to lowercase using text[0].lower(), it becomes 'h'. 
# The lowercase letter 'h' is at index 7 in the string alphabet ('abcdefghijklmnopqrstuvwxyz'). Therefore, the output of print(index) will be 7.

#step 16: Declare a variable named shifted and assign it the alphabet letter at index plus shift.
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)
shifted = alphabet[index+shift]
#step 17: print it
print(shifted)
#output: k
