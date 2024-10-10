"""
Ask a number from user

if number divisible by 3 -> FIZZ
if number divisible by 5 -> BUZZ
if number divisible by 3 and 5 -> FIZZBUZZ
else FIZZFIZZBUZZBUZZ


3 
FIZZ

5
BUZZ

15
FIZZBUZZ
"""

num = int(input("Enter a number = "))
if num % 3 == 0 and num % 5 == 0:
    print("FIZZBUZZ")
elif num % 3 == 0:
    print("FIZZ")
elif num % 5 == 0:
    print("BUZZ")
else:
    print("FIZZFIZZBUZZBUZZ")
