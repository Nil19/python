#Step 1: Start by defining a function named add_expense that takes three parameters: expenses, amount and category. Use the pass keyword to fill the function body.

def add_expense(expenses, amount, category):

    pass

#Step 2: Create an empty list named expenses. You will use it to store each of your expenses.
expenses = []

#Step 3: Replace pass with a call to the .append() method on the expenses list. Don't pass any arguments to .append() for now.

def add_expense(expenses, amount, category):
    expenses.append()

#Step 4: Create a dictionary with a key 'amount' and value of the amount parameter and pass your new dictionary to the .append() call.
#Step 5: Use the string 'category' as the key, and the category parameter as the value.
    expenses.append({'amount': amount, 'category': category})

#Step 6: Start by defining a function named print_expenses that takes one parameter expenses. This function will later be used to display each expense in your list.
#Fill the body of your new function with a pass statement.

def print_expenses(expenses):

    pass

#Step 7: Inside the print_expenses function, create a for loop that iterates over each item in the expenses list. Use expense as the loop variable and move pass inside the loop body.

def print_expenses(expenses):
    for expense in expenses:    
        
        pass

#Step 8: Inside the for loop, replace pass with a print() call and pass it the following f-string: f'Amount: {expense}, Category: {expense}'. Leave the placeholders empty for now.
        print(f'Amount: {expense}, Category: {expense}')

#Step 9: You are currently interpolating the expense dictionary in your f-string. 
#Modify the f-string expression to access the value of the 'amount' key and the 'category' key in the expense dictionary.
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

#Step 10: Define a function named total_expenses that takes one parameter expenses. Fill the function body with a pass statement for now.

def total_expenses(expenses):
    
    pass