# Exercise 10: Create a new list from two list using the following condition
# Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# pseudocode

# Add odd numbers from the first list
# Add even numbers from the second list
# Sample list
# Result


# -------------------------------------- actual code ---------------------------------------------------


def create_new_list(list1, list2):
    new_list = []
    
    # Add odd numbers from the first list
    for num in list1:
        if num % 2 != 0:
            new_list.append(num)
            
            
# Add even numbers from the second list
# Sample list
# Result