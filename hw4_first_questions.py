
############################### Question 1 ############################################

# the function 'triple' will take in a value x as argument and
# return the value of x multiplied by 3

def triple(x):
    try:
        print("The argument entered is {x}".format(x = x))
        print("Data Type of the argument is {dtype}".format(dtype = type(x)))
        print("The result after multiplying the argument by 3 equals {result}:".format(result = 3*x))
        return (3*x)
    except Exception as error:
        print("Error",error)


#triple(3)
#triple("a")
#triple(['a','b','c'])
#triple({"a":1})


############################### Question 2 ############################################

# the funciton "subtract" will take two arguments and
# return the result of the second subutracted from the first

def subtract(a,b):
    try:
        print("The first argument entered is {a} and the second argument is {b}".format(a=a ,b=b))
        print("Data Type of the arguments is {dtype1} and {dtype2}".format(dtype1 = type(a),dtype2 =type(b)))
        print("The result [second - first] equals {result}:".format(result = a - b))
        return (a-b)

    except Exception as error:
        if type(a) != type(b):
            print("Error: Data type of the arguments is different.")
        else:
            print("Error: Subtraction operation not defined for the argument")

#subtract(['a','b'],['a'])
#subtract(2,'2')


############################### Question 3 ############################################

# Create a function called "dictionary_maker" that has one parameter: a list of 2-tuples.
# It should return the same data in the form of a dictionary, where the first element
# of every tuple is the key and the second element is the value.
def dictionary_maker(list_tuples):
    list_dict = list()
    try:
        print("List of tuples provided:", list_tuples)
        for tuple in list_tuples:
            key,value = tuple
            d = {key:value}
            list_dict.append(d)
        print("resulting list of dictionary :",list_dict)
        return (list_dict)
    except Exception as error:
        print(error)

#dictionary_maker([('a',0),('b',1)])