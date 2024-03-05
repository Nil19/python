#Step 17: Within the verify_card_number function, create a variable odd_digits that contains every other digit of the card_number_reversed string.
#Step 18: Print the value of the odd_digits variable to the console.
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    print(odd_digits)

#Step 19: Use a for loop to iterate over each digit in the odd_digits list. 
# Move your print call from the previous step into the for loop, and change it to print each digit.
    
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
       odd_digits = card_number_reversed[::2]
    print(digit)

#Step 20: Within the for loop, use the += operator to add the digit to the sum_of_odd_digits variable.
    for digit in odd_digits:
        sum_of_odd_digits += digit
        print(digit)

#Step 21: Convert the digit variable to an integer before adding it to sum_of_odd_digits. 
# Then, move the print call to the end of the verify_card_number function to print the value of sum_of_odd_digits.
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    print(sum_of_odd_digits)

#Step 22: Below your print call, create a variable named sum_of_even_digits and assign it a value of 0.
    sum_of_even_digits = 0

#Step 23: Create a variable even_digits and assign it the even digits of the reversed card number.
    even_digits = card_number_reversed[1::2]

#Step 24: Loop over the even digits and print each to the console.
    for digit in even_digits:
        print(digit)
    
#Step 25: Remove the print call for the sum of the odd digits.
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        print(digit)
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    verify_card_number(translated_card_number)

main()