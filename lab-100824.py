def assignment_operator():
    #Assignment Operators
    a = 11
    a += 5
    print(a)


    #testing with subtraction
    b = 11
    b -= 5
    print(b)

    #testing with floor division
    c = 11
    c //= 5
    print(c)

def comparison_operators():
    #example
    a = 11
    b = 5
    result = a < b
    type_result = type(result)
    print(f"result = {result} and its data type is {type_result}")

    #negative operator
    a = 11
    b = 5
    result = a != b
    type_result = type(result)
    print(f"result = {result} and its data type is {type_result}")

    #with equals
    a = 11
    b = 5
    result = a == b
    type_result = type(result)
    print(f"result = {result} and its data type is {type_result}")

def strings():
    greeting_string= "Welcome to Programming unit! This is level 4 unit:)"
    print(greeting_string)
    #index starts at 0 so 1st postition is 0 and 5th is actually 4
    print(greeting_string[0], greeting_string[4])
    #printing a range of characters from the string
    print(greeting_string[0:5])
    #using negative indexing to print -1
    print(greeting_string[-1])
    #using a negative index to do last 4 digits
    print(greeting_string[-4:])
    #strings are immuatable / cannot be edited
    #remove the # on the next line to try edit, it causes an error
    #greeting_string[0] = "X"

def data_types():
    print(type(11.0))
    print(type(11))
    print(type("11" + "11"))
    print(type("a"))
    print(type(True))
    print(type("False"))

def type_conversion():
    #converting a float into an int
    x = 10.5
    print(type(x))
    x = int(x)
    print(type(x))

    x ="A string"
    y = 10 
    z = 5.5

    print(type(y+z))
    print(type(y+int(z)))
    print(type(z+float(y)))
    print(str(z))
    print(type(x+str(y)+str(z)))
    #print(x+y) # this is a type error

def illegal_assignment():
    #all are errors
    '''
    my-var = 1
    my_var$ = 1
    my_var_& = 1
    2my_var = 1
    #this is good:
    my_var = 1
    '''

def number_pattern():
    number = int(input("user number"))
    print (str(number) * number)

from numpy import random

def selection_sort():
    array = ""
    array = random.randint(100, size=(10))
    for i in range(len(array)):
        for x in range(len(array-i)):
            if array[i] < array[x]:
                array[i], array[x] = array[x], array[i]
    print(array)
    
selection_sort()