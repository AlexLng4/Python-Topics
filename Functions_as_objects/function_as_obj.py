# in python function are objects (means first class object)
# important!! methods are created and called using a class
# function are just function :) def or lambda
def factorial(n):

    return 1 if n<2 else n*factorial(n-1) 

# sort a list with a lambda
fruits = ["banna","apple", "orange"]
fruits = sorted(fruits, key=lambda word: word.upper())
print(fruits) 



print("Stop")