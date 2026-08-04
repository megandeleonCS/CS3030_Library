"""
=========================================================
Lab Title: Python Advanced Lab
Author: [Your Name Here]
Date: [Insert Date Here]
Description: Lab covers advanced Python concepts.
=========================================================
"""

# Use a list comprehension to generate a list of squares for all even numbers between 1 and 20 (inclusive).
# TODO 1: List comprehension for squares of even numbers from 1 to 20

# Use a dictionary comprehension to create a dictionary where keys are numbers from 1 to 5 and values are their cubes (e.g., {1: 1, 2: 8, ...}).
# TODO 2: Dictionary comprehension for numbers 1 to 5 and their cubes

# Write a generator function named fibonacci_gen(n) that yields the first n numbers of the Fibonacci sequence using the yield keyword.
# TODO 3: Define generator function fibonacci_gen(n)

# Write a generator expression that yields the lengths of each word in the list ["advanced", "python", "generator", "expression"]. Loop through and print the results.
words = ["advanced", "python", "generator", "expression"]
# TODO 4: Create a generator expression for word lengths and print them
 
#Create a decorator function named log_execution that prints "Executing function..." before the target function runs and "Execution complete." after it finishes. Apply it to a simple function using the @ syntax.
# TODO 5: Create and apply the log_execution decorator

# Write a function named sum_all that accepts an arbitrary number of positional arguments (*args) and returns their total sum.
# TODO 6: Write sum_all using *args

# Use the built-in sorted() function combined with a lambda function to sort a list of tuples [("apple", 5), ("banana", 2), ("cherry", 9)] based on the numeric value (the second element of each tuple).
items = [("apple", 5), ("banana", 2), ("cherry", 9)]
# TODO 7: Sort list of tuples using sorted() and a lambda function

# Create a class named BankAccount. It should have an __init__ method that takes owner and an initial balance (defaulting to 0.0).
# Add a method named deposit(amount) to BankAccount that adds to the balance, and a method named withdraw(amount) that subtracts from it (ensuring the balance doesn't drop below zero).
# TODO 8 & 9: Define BankAccount class with init, deposit, and withdraw methods

# Create a subclass named SavingsAccount that inherits from BankAccount, adding an attribute interest_rate and a method apply_interest() that increases the balance by the interest rate percentage.
# TODO 10: Define SavingsAccount subclass inheriting from BankAccount