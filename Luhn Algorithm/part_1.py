#Working with Numbers and Strings by Implementing the Luhn Algorithm
#Step 1: declare a function called main. Use the pass keyword to avoid an error.

def main():
    pass

#Step 2: Replace the pass statement with a variable named card_number and a value of 4111-1111-4555-1142.
def main():
    card_number = "4111-1111-4555-1142"

#Step 3: Create a variable called card_translation and assign it a translation table to replace all - and characters with an empty string.
    card_translation = str.maketrans({'-': '', ' ': ''})

#Step 4: Create a variable called translated_card_number and assign it the result of calling the translate method on card_number with card_translation as an argument.
    translated_card_number = card_number.translate(card_translation)

#Step 5: Print the translated card number to the console.
#Step 6: Call the main function at the end of your script.
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    print(translated_card_number)
main()

