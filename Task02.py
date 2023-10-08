# Prediction Game

import random
i =0
n=3

random_num = random.randint(0,6)
print("Welcome in the prediction game\nYou have three attempts to predict my number\n")
for i in range(3):
    i += 1

    print("Predict my number in range from 0 to 6 : ")
    user_num = int(input())

    if user_num == random_num:
        print("CONGRATULATIONS!!!\nYour prediction is correct ,my number is",random_num)
        break
    else:
        n -=1
        print("Your prediction is not correct,You have ", n, "attempts left Try again\n")
        if user_num < random_num:
            print("hint : my number is more than",user_num)
        else:
            print("hint : my number is less than",user_num)

if n == 0:
    print("GAME OVER")

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