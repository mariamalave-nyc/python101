# Author: Maria Malave
#Date: 01/10/2020 - updated 01/20/2020

def greet(first_name, last_name, middle_name, age):
    greeting = 'My name is ' + last_name + ', ' + first_name + ' ' + middle_name +' ' + last_name  + ' and my age is ' + age + '!'
    return greeting
 

# Replace with your first and last name.
# That is, unless your name is already James Bond.
'''greet('James', 'Bond', 'John')
'''
print(greet('James', 'Bond', 'John', '50')) 
