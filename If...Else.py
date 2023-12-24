# If Statement #

number1 = 39
number2 = 49

if number1 > number2:
    print("number1 is greater than number2")  #

if number1 < number2:
    print("number1 is less than number2")  # number1 is less than number2

# Nested If Structures #

number3 = 99

if number3 > 50:
    print("Number3 is above fifty,")
    if number3 > 80:
        print("and also above eighty,")
        if number3 < 100:
            print("and also below a hundred.")  # Number3 is above fifty,
            # and also above eighty,
            # and also below a hundred.

# Elif #

number1 = 39
number2 = 49
number3 = 99
number4 = 99

if number3 > number4:
    print("number3 is greater than number4")
elif number3 == number4:
    print("number3 and number4  are equals")  # number3 and number4  are equals

# Else #

number1 = 39
number2 = 49
number3 = 99

if number1 > number2:
    print("number1 is greater than number2")
elif number1 == number2:
    print("number1 and number2 are equal")
else:
    print("number2 is greater than number1")  # number2 is greater than number1

# if is in function #

list1 = []


def sequence(r):
    if r > 0:
        result = r + sequence(r - 1)
        list1.append(result)
    else:
        result = 0
    return result


sequence(10)  # 55 and list1 = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

sequence(17)  # 153 and list1 = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153]


def periodic_function(x):
    if 0 < x <= 5:
        return x + 3
    elif x > 5:
        return periodic_function(x-5)
    else:
        print("Input must be bigger than zero")


periodic_function(4)  # 3
periodic_function(5)  # 8
periodic_function(13)  # 6
periodic_function(31)  # 4
periodic_function(3.5)  # 6.5




