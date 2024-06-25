#Step 1: define a new function named convert_to_snake_case() that takes pascal_or_camel_cased_string as input. 
#Within the function body, include a pass statement to temporarily fill the function body.
def convert_to_snake_case(pascal_or_camel_cased_string):
    pass

#Step 2: Inside the function, replace the pass statement by creating an empty list named snake_cased_char_list.
    snake_cased_char_list = []

#Step 3: Inside the function, below the list you just created, add a for loop to iterate through the pascal_or_camel_cased_string. 
#Make sure to name the target variable char. For now, add a pass statement as a placeholder in the loop body.
    for char in pascal_or_camel_cased_string:

        pass

#Step 4: Inside the for loop, add an if statement to check if the current character is uppercase. Move the pass statement inside the new if statement.
        if char.isupper():
        
            pass

#Step 5: Use the .lower() string method to convert uppercase characters to lowercase characters. 
#Then, prepend an underscore to the character. Assign the results to a variable named converted_character
        if char.isupper():
           '_' + char.lower()
           converted_character = '_' + char.lower()

#Step 6: Use the .append() method on the snake_cased_char_list to add the converted_character to the list.
            snake_cased_char_list.append(converted_character)

#Step 7: Right after the if statement within the for loop, add an else clause and use the .append() method to add char to the snake_cased_char_list variable.
        else:
            snake_cased_char_list.append(char)

#Step 8: use the .join() method to join the elements in snake_cased_char_list using an empty string as the separator. 
#Assign the result to a new variable named snake_cased_string.
    snake_cased_string = ''.join(snake_cased_char_list)

#Step 9: eclare a new variable named clean_snake_cased_string and assign it the result of the .strip() method applied to snake_cased_string , 
#passing '_' as the argument to the method.
    clean_snake_cased_string = snake_cased_string.strip('_')

#Step 10: Add a return statement at the end of the function to return the clean_snake_cased_string.
    return clean_snake_cased_string