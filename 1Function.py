# Function Structures #


def function0():
    print("Hello, I am a function")


function0()  # Hello, I am a function


def function1(x):
    print(x + 99)


function1(1)  # 100
function1(88)  # 187


def function2(x):
    print(x ** x)


function2(3)  # 27
function2(5)  # 125


def function3(x, y):
    print(x * y)


function3(5, 18)  # 90
function3(13717421, 9)  # 123456789


def function4(x, y=7):
    print((x + y) * 2)


function4(3)  # 20
function4(53)  # 120


def function5(x, y):
    print(x + " " + y)


function5("Bilgehan", "Yaylali")  # Bilgehan Yaylali
function5("Data", "Science")  # Data Science


# Arbitrary Arguments #

def function6(*colors):
    print("My favorite color is " + colors[3])


function6("red", "black", "purple", "blue", "yellow")  # My favorite color is blue

# List with function #

empty_list = []


def function7(x):
    empty_list.append(x)
    print(empty_list)


function7(99)  # [99]
function7(101)  # [99,101]
function7("Bilgehan")  # [99,101,'Bilgehan']


# Return Values #

def function8(x):
    return x + 10


function8(5)  # 15
function8(5) * 2  # 30


def function9(x, y, z):
    a = (x ** 2) + (3 * x) + 5
    b = (y ** 2) + (5 * y) + 4
    c = (z ** 2) + (7 * z) + 3
    k = a + b + c
    return a, b, c, k


function9(1, 2, 3)  # (9, 18, 33, 60)
function9(1, 2, 3) * 2  # (9, 18, 33, 60, 9, 18, 33, 60)


# Nested functions #

def nested1(x, y, z):
    return int(x + y + z) / 3


def nested2(p, k, l):
    return p ** k, p ** l


def nested(x, y, z, k, l):
    a = nested1(x, y, z)
    b = nested2(a, k, l)
    print(b)


nested(1, 2, 3, 5, 7)  # (32.0, 128.0)
nested(1, 3, 4, 1, 2)  # (2.6666666666666665, 7.111111111111111)


def nested11(x, y):
    return x + y


def nested22(z, k, l, m, n):
    return (k + l) * (m - n) / z


def nested33(x, y, k, l, m, n):
    a = nested11(x, y)
    b = nested22(a, k, l, m, n)
    print(b)


nested33(1, 2, 3, 4, 5, 6)  # -2.33333333333333335
nested33(0, 1, 5, 6, 7, 3)  # 44.0
