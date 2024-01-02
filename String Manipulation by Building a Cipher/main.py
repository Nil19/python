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