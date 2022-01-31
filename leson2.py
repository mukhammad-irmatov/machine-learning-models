def function1():
    number = int(input("Enter a number: "))
    if(number>0):
        print("{} is positive".format(number))
    elif(number==0):
        print("{} is not negative and positive".format(number))
    else:
        print("{} is negative number".format(number))
def maxNumber():
    number1 = int(input("enter a number: "))
    number2 = int(input("enter a number: "))
    number3 = int(input("enter a number: "))
    if(number1>number2 and number1>number3):
        print("largest number is ",number1)
    elif(number2>number1 and number2>number3):
        print("largest number is ",number2)
    else:
        print("largest number is ", number3)

# reversed_number = 0
# def NumberReverse(num):
#     global reversed_number
#     if num!=0:
#         remainder=num%10
#         reversed_number=(reversed_number*10)+remainder
#         NumberReverse(num//10)
#     return reversed_number
#
# number=int(input("Enter your Number:"))
# if(NumberReverse(number)==number):
#     print(number," is a Palindrome Number.")
# else:
#     print(number," is not a Palindrome Number.")



number = input("enter a number: ")
if number==number[::-1]:
    print("{} is palindrome".format(number))
else:
    print("{} is not palindrome".format(number))
























