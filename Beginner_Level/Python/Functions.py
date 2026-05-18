# built-in

# abs
# my_list = abs(-10.58)
# print(my_list)

# len
# list1 = ["V", "A", "M", "S", "I"]
# x = len(list1)
# print(x)

# all
# my_list = [1, 0, 1]
# x = all(my_list)
# print(x)

# sum
# s = sum([20, 35, 70])
# s1 = sum((7, 5, 9))
# print(s)
# print(s1)

# max and min
# m1 = max([21, 99, 55, 75, 69, 84])
# print(m1)
# m2 = min({21, 99, 55, 75, 69, 84})
# print(m2)

# iter
# list1 = iter(["V", "A", "M", "S", "I"])
# x = next(list1)
# print(x)
#
# x = next(list1)
# print(x)

# pow
# x1 = pow(3, 3)
# x2 = pow(2, 4)
# print(x1)
# print(x2)

# range
# x = range(6)
# for n in x:
#     print(n)

# round
# x = round(8.726548, 3)
# print(x)

# sorted
# a = ["V", "A", "M", "S", "I"]
# x = sorted(a, reverse = True)
# print(x)

# a = [5, 12, 56, 4, 99]
# x = sorted(a, reverse=True)
# print(x)


# User-defined

# def my_function(country="Norway"):
#     print("I love " + country)


# my_function("Sweden")
# my_function("London")
# my_function()


# def add(num1):
#     print(5+num1)
#
# add(5)


# def add(n1,n2):
#    result=n1+n2
#    print("the sum of numbers", result)


# number1 = 9.88
# number2 = 10.45
#
# add(9.88, 10.45)


# def add(number1, number2):
#     return number1+number2
#
#
# print(add(1, 2))


def greetMe(name):
    print("Good Morning "+name)

greetMe("Vamsi")