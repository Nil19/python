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