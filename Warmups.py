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
