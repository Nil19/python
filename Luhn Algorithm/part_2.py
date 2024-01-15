#Step 7: Define a function verify_card_number with a parameter card_number, and use the pass keyword to make the function do nothing.
def verify_card_number(card_number):
    pass

#Step 8: Within your main function, call the verify_card_number function and pass in the translated_card_number variable as an argumen
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
    
