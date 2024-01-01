# Author: Greg
print("hello world")

# variables
my_var = 2+3
print("value is", my_var, sep=":")
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_range = range(1, 6)
my_set = {1, 2, 3, 4, 5}
print(my_list, my_tuple, my_range, my_set, sep="\n")
my_dict = {"name": "John", "age": 36}
my_dict["name"] = "John Doe"
print(my_dict)

'''
functions
'''
def greet(name):
    print(f"Hello, {name}!")

greet("World")