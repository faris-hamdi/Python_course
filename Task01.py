# Calculator

operation = int(input("1 - (ِِAddition)\n2 - (Subtraction)\n3 - (Multiplication)\n4 - (Division)\n5 - (Power)\n6 - (Decimal to Binary Conversion)\nEnter the operation number: "))


def sum_fun(num1, num2):
    return num1 + num2


def sub_fun(num1, num2):
    return num1 - num2


def mul_fun(num1, num2):
    return num1 * num2


def div_fun(num1, num2):
    return num1 / num2


def pow_fun(num1, num2):
    result = 1
    for n in range(num2):
        result *= num1

    return result


def bin_fun(dec_num):
    result = bin(dec_num)
    return result


if operation <= 5:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if 1 == operation:
        print(num1," + ",num2," = ", sum_fun(num1, num2))

    elif 2 == operation:
        print(num1," - ",num2," = ", sub_fun(num1, num2))

    elif 3 == operation:
        print(num1," * ",num2," = ", mul_fun(num1, num2))

    elif 4 == operation:
        print(num1," / ",num2," = ", div_fun(num1, num2))

    elif 5 == operation:
        print(num1," ^ ",num2," = ",pow_fun(num1, num2))
else:
    print("Enter your Decimal number: ")
    dec_num = int(input())
    print(dec_num," in binary"," = ",bin_fun(dec_num))