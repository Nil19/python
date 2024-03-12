#Step 11: Create a test variable and assign it a lambda function that takes an x parameter and returns x * 2.

test = lambda x: x * 2

#Step 12: Call your test lambda function and pass 3 as the argument. Then, print the result.
print(test(3))

#Step 13: Modify your print() call to print the result of calling map() with test as the first argument, and [2, 3, 5, 8] as the second argument.

print(map(test, [2, 3, 5, 8]))

#Step 14:  modify your current print() call by passing sum(map(test, [2, 3, 5, 8])) as the argument.
print(sum(map(test, [2, 3, 5, 8])))

#Step 15: For now, delete both the test function and the print() call.

#Step 16: Within your total_expenses function, replace pass with a lambda function. Use expense as the parameter and return the value of the 'amount' key in the expense dictionary.
def total_expenses(expenses):
    lambda expense: expense['amount'] 

#Step 17: Now, call map() passing your lambda function as the first argument and the expenses list as the second argument.
    map(lambda expense: expense['amount'], expenses)

#Step 18: Finally, pass your map() call to the sum() function to obtain the total expenses and return the result.
    return sum(map(lambda expense: expense['amount'], expenses))

#Step 19: Next, define a function named filter_expenses_by_category that takes two parameters: expenses and category. Use pass to fill the function body.
def filter_expenses_by_category(expenses, category):
    
    pass

#Step 20: Within the filter_expenses_by_category function, replace pass with a lambda function. Use expense as the parameter and return the comparison between the value of the 'category' key of the expense dictionary and category.
def filter_expenses_by_category(expenses, category):
    lambda expense: expense['category'] == category