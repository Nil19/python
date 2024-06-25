#Step 11: Create a new function called main() with pass as the body of the function.
def main():
    
    pass

#Step 12: replace the pass statement, with a call to the convert_to_snake_case() function, passing the string 'aLongAndComplexString' as input.
#To display the output, pass the function call as the argument to the print() function.
    print(convert_to_snake_case('aLongAndComplexString'))

#Step 13: Call the main() function.
main()

#Step 14: Comment out all the lines of code inside the convert_to_snake_case() function and add a pass
def convert_to_snake_case(pascal_or_camel_cased_string):
    # snake_cased_char_list = []
    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #       converted_character = '_' + char.lower()
    #       snake_cased_char_list.append(converted_character)
    #     else:
    #         snake_cased_char_list.append(char)
    # snake_cased_string = ''.join(snake_cased_char_list)
    # clean_snake_cased_string = snake_cased_string.strip('_')

    # return clean_snake_cased_string
    pass

#Step 15: Replace the pass keyword with the variable snake_cased_char_list and assign it an empty list. Use the square brace notation to create the list.
    snake_cased_char_list = []

#Step 16: You will need to convert uppercase characters to lowercase and add an underscore before them. Use the return statement to return the list snake_cased_char_list from your function.
    return snake_cased_char_list

#Step 17: Modify the return statement to return the result of joining snake_cased_char_list with an empty string as a separator.
    return ''.join(snake_cased_char_list)

#Step18: Add a call to the .strip() method to remove any leading or trailing underscores.
    return ''.join(snake_cased_char_list).strip('_')

#Step 19: Turn your empty list into a list comprehension that converts each character in pascal_or_camel_cased_string into a lowercase character and prepends an underscore to it. 
#Use char to iterate over pascal_or_camel_cased_string
    snake_cased_char_list = ['_' + char.lower() for char in pascal_or_camel_cased_string]

#Step 20: Add an if clause to your list comprehension so that the expression is executed only if the character is uppercase.
    snake_cased_char_list = ['_' + char.lower() for char in pascal_or_camel_cased_string if char.isupper()]

#Step 21: You need to execute a different expression for the characters filtered out by the if clause. You'll use an else clause for that.
    snake_cased_char_list = ['_' + char.lower() if char.isupper() else char for char in pascal_or_camel_cased_string]

#Step 22: Get rid of the commented lines of code inside the convert_to_snake_case() function to clean up the function definition.
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string

#Step 23: inally try out this new implementation by executing the program. 
#Change the input string to 'IAmAPascalCasedString' and see if it comes out as 'i_am_a_pascal_cased_string', even though that's a lie.
def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))