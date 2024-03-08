#Step 26: Within the even digit for loop, replace the print call with a variable named number and assign it 
# the value of digit multiplied by 2.

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2

#Step 27: To prevent the multiplication of one digit from being greater than 9, within the even digit loop,  
# add an if statement that checks if number is greater than or equal to 10. If it is, print number.

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
    if number >= 10:
        print(number)

#Step 28: Within the if statement, assign number the result of number // 10 (integer division) plus the modulus of number and 10.
    if number >= 10:
        print(number)
        number = number // 10 + number % 10

#Step 29: Move the print call below the number reassignment
#Step 30: Outside of the if statement, add number to sum_of_even_digits. Also, remove the print call.
    if number >= 10:
        number = (number // 10) + (number % 10)
    sum_of_even_digits += number

#Step 31: Below the second for loop of the verify_card_number function, create a variable named total, and assign it the value of the sum of the odd and even digits. Print total to the console.
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)

#Step 32 Return the result of comparing 0 to total modulo 10
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    return 0 == total % 10

#Step 33: Adjust the verify_card_number call such that if it returns True, print 'VALID!' to the console. Otherwise, print 'INVALID!'.
   if verify_card_number(translated_card_number):
        print('VALID!')
    else: 
        print('INVALID!')

#Step 34: Change the value of card_number such that 'INVALID!' is printed to the console.
def main():
    card_number = '4111-1111-4555-1442'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

#Step 35: As a final step, remove the print call from the verify_card_number function, and change the card_number back to something valid.