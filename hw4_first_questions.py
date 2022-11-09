# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#

def triple(x):
    x = x*3
    return x
# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#
def subtract(x, y):
    a = x - y
    return a

# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}


def dictionary_maker(x:tuple):
    x = dict(x)
    return x
    
