print("******* welcome to the zodiac calculator *******")
print("enter the number 1 :")
num1=int(input())
print("enter the number 2 :")
num2=int(input())
print(" these are the operators you can use :")
print("1. Addition")
print("2. substraction")
print("3. multiplication")
print("4. division")
print("5. modulus")
operator=input("choose an option from these(1,2,3,4,5):")
if operator=="1":
    print("this is an addition operation")
    print("the sum of two numbers is :",num1+num2)
if operator == "2":
    print("this is a subtraction operation")
    print("the difference of two numbers is :", num1-num2)
if operator == "3":
    print("this is a multiplication  operation")
    print("the product of two numbers is :", num1*num2)
if operator == "4":
    print("this is a division operation")
    print("the divident of two numbers is :", num1/num2)
if operator == "5":
    print("this is a modulus operation")
    print("the modulus of two numbers is :", num1%num2)

