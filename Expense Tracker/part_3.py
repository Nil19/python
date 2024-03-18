#Step 31: Pass input('Enter amount: ') to the float() function.
        
        if choice == '1':
            amount = float(input('Enter amount: '))

#Step 32: Inside your if statement, create a variable category to store the expense category. Assign it input('Enter category: ').
            category = input('Enter category: ')

#Step 33: call the add_expense function, passing three arguments: expenses, amount and category.
            add_expense(expenses, amount, category)

#Step 34: 
        elif choice == '2':
            print('\nAll Expenses:')

#Step 35: After the print() call, call the print_expenses function to display all the expenses that have been added so far. Pass the expenses list as the argument.
            print_expenses(expenses)

#Step 36: create an elif statement that checks if choice == '3'.

#If it's true, it means the user wants to see the total expenses. So call print() and pass the string '\nTotal Expenses: ' as the first argument and total_expenses(expenses) as the second argument.
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
            print(total_expenses(expenses))

#Step 37: Create another elif statement that checks if choice == '4'. Inside the new elif, create a variable category and assign it input('Enter category to filter: ') to filter the expense category.
        elif choice == '4':
            category = input('Enter category to filter: ')

#Step 38: After getting the category, print the following f-string f'\nExpenses for {category}:'.
            print(f'\nExpenses for {category}:')

#Step 39: After your print() call, you need to filter the expenses and print the filtered list. Declare a variable expenses_from_category and assign it a call to filter_expenses_by_category passing expenses and category as the argument.
            expenses_from_category = filter_expenses_by_category(expenses, category)

#Step 40: Still within the elif statement, pass expenses_from_category iterator to a print_expenses call.
            print_expenses(expenses_from_category)

#Step 41: use another elif statement to check if choice equals the string '5'.
#Inside the new elif statement, print the string 'Exiting the program.' to show that the program is terminating its execution.
        elif choice == '5':
            print('Exiting the program.')

#Step 42: Finally, to stop the execution of the while loop, add the break statement inside your last elif statement.
            break

#Step 43: Finally, call your main() function, and try the expense tracker program.
main()

#Step 44: If the value of __name__ is set to '__main__', it implies that the current script is the main program, and not a module.
#As a final step, create an if statement to check if __name__ == '__main__', and move the main() call inside this block.
if __name__ == '__main__':
    main()

