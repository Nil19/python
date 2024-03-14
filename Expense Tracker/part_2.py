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

#Step 21: Within the filter_expenses_by_category function, call filter() passing the lambda function you wrote in the previous step as the first argument and the expenses list as the second argument.    
def filter_expenses_by_category(expenses, category):
    filter(lambda expense: expense['category'] == category, expenses)

#Step 22: Finally, return the result of the filter() call
    return filter(lambda expense: expense['category'] == category, expenses)

#Step 23: Define a function named main without parameters. Fill the function body with the expenses list you created at the beginning of this project. You will use this list to store the expense records.
def main():
    expenses
    pass
expenses = []

#Step 24: create a while loop. Use True for the condition, and print the string '\nExpense Tracker' inside the loop body to show the title of the program.
#Step 25: After the print() call, add another one to print the string '1. Add an expense'.
#Step 26: Next, add another print() call and pass the string '2. List all expenses'.
#Step 27: Provide the other menu options by printing the following three strings in your while loop: '3. Show total expenses', '4. Filter expenses by category', and '5. Exit'.
def main():
    expenses = []
    while True: 
        print("\nExpense Tracker")
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

#Step 28: Inside your while loop, call the input() function passing the string 'Enter your choice: ' as the argument, and assign the result to a variable named choice.
        choice = input('Enter your choice: ')