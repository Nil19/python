#Step 26: Within the even digit for loop, replace the print call with a variable named number and assign it the value of digit multiplied by 2.

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2