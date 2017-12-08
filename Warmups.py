# New python File: Warmups.py

# 12.4.17
# Write a Python function
# which accepts the user's
# first and last name
# and print them in reverse order
# with a space between them.


def reverse_order(first_name, last_name):
    # print("%s, %s" % (last_name, first_name))
    print(last_name + " " + first_name)  # Concatenation


# 12.5.17
"""Write a function called add_py
that takes one parameter called "name"
and prints out name.py
example:
add_py("John") == "John.py"
"""
def add_py(name):
    print("%s.py" % name)  # Solution 1
    print(name + ".py")  # Solution 2


# 12.6.17
"""Write a function called "add"
which takes three parameters 
and prints the sum of the numbers
"""


def add(num1, num2, num3):
    print(num1 + num2 + num3)

add(15, 18, 9000)
add(80, 90, 100)


# 12.7.17
# Write a function called "repeat"
# that takes one parameter (string)
# and prints it three times.
#
# example:
# repeat("Hello") prints:
# Hello
# Hello
# Hello

def repeat(sentence):
    print(sentence)
    print(sentence)
    print(sentence)

    print(sentence + "/n" + sentence + "/n" + sentence + "/n")

    for x in range(3):
        print(sentence)

# 12.8.17
"""
Write a function called "date"
that takes in three parameters,
"month", "day", and "year" and 
prints out the date, separated by a "/"

example:
date(12, 8, 17) == "12/8/17"
"""