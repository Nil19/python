#Step 7: Define a function verify_card_number with a parameter card_number, and use the pass keyword to make the function do nothing.
def verify_card_number(card_number):
    pass

#Step 8: Within your main function, call the verify_card_number function and pass in the translated_card_number variable as an argument
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    verify_card_number(translated_card_number)
    print(translated_card_number)

#Step 9; The Luhn algorithm is as follows:

# From the right to left, double the value of every second digit; if the product is greater than 9, sum the digits of the products.
# Take the sum of all the digits.
# If the sum of all the digits is a multiple of 10, then the number is valid; else it is not valid.
    
# Account number      7   9  9  2  7  3  9   8  7  1  x
# Double every other  7  18  9  4  7  6  9  16  7  2  x
# Sum 2-char digits   7   9  9  4  7  6  9   7  7  2  x
    
# Replace the pass statement with a variable sum_of_odd_digits and a value of 0.
def verify_card_number(card_number):
    sum_of_odd_digits = 0 

#Step 10: Create a variable named card_number_reversed and assign it the value of the first 4 characters of card_number.
    card_number_reversed = card_number[0:4]

#Step 11: Print the value of the card_number_reversed variable to the console.
    print(card_number_reversed)

#Step 12: Change card_number_reversed to be every second digit of the first four digits of card_number
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[0:4:2]
    print(card_number_reversed)

#Output:
    # 4111111145551142
    # 41

#Step 13: Reverse the order of the digits in the last four digits of card_number, by using a slice with a step of -1. You can use either negative or positive indices for the start and end indices.
    card_number_reversed = card_number[-1:-5:-1]

#Output:
    # 4111111145551142
    # 2411

#Step 14: Assign the reverse of the full card_number string to the card_number_reversed variable.
    card_number_reversed = card_number[::-1]

#Output: 
    # 4111111145551142
    # 2411555411111114

#Step 15: Remove the print call from the verify_card_number function.
#Step 16: Remove the print call from the main function.