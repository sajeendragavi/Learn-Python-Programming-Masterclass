# a = 12
# b = 3
#
# print(a + b)
#
# numbers= "1, 2, 3, 4, 5, 6, 7, 8, 9"
# print(numbers[0::3])
#
# age = 26
# print("My age is {0} years".format(age))
#
# name = input("please enter your name:")
# age = int(input("how old are you {}?".format(name)))
# print(age)
#
#
# if age >= 18:
#     print("You are old enough to vote")
#     print("please put an X in the box")
#
# else :
#     print("please come back in {0} years".format(18 - age))

# print("please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess < 5:
#     print("please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("Well done,you guessed correctly")
# elif guess > 5:
#     print("please guess lower ")
#     guess = int(input())
#     if guess == 5:
#         print("you have guessed it correctly")
#     else :
#         print("sorry, you have not guessed it correctly")
# else:
#     print("you got it first time")

# age = int(input("How old are you :"))
# if not(age < 18):
#     print("YOu are old enough to vote")
#     print("please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))

name = input("what is your name :")
age = int(input("how old are you ,{}:".format(name)))

if (age >= 18) and (age < 31) :
    print("welcome to the holidays")
else :
    print("sorry,you have not qullified the entry")
