# wap to get fibonacci upto 10 numbers
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,11):
#     c=a+b
#     a=b
#     b=c
#     print(c)

# wap to check prime numbers
# num=int(input("enter a number here"))
# if num<=1:
#     print("it is not a prime num")
# else:
#     for i in range(2,num):
#         if num%2==0:
#             print("number is not a prime number")
#             break
#         else:
#             print("it is prime number")
#             break

# wap to check palindrome
# num =int(input("enter a number here"))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
#
# if rev==temp:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

# wap to make area calculator
print("********Area claculator**************")
while True:
    print("""press 1 to get area of square
    press 2 to get area of rectangle
    press 3 to get area of circle
    press 4 to get area of triangle""")
    choice=int(input("enter a number between 1-4:"))
    if choice==1:
        while True:
            side =float(input("enter the length of one side"))
            area=side*side
            print("The area od square is ",area)
            repeat=input("do you want to try again with sq?")
            if repeat=="no":
                break
    elif choice==2:
        while True:
            length=float(input("enter the length of rect"))
            breadth=float(input("enter the breadth of rect"))
            area=length*breadth
            print("The area of circle is",area)
            repeat=input("do you want to try again with sq?")
            if repeat=="no":
                break
    elif choice==3:
        while True:
            radius=float(input("enter the raduis of circle"))
            area=(22/7)*radius**2
            print("The area of circel is",area)
            repeat=input("do you want to try again with sq?")
            if repeat=="no":
                break
    elif choice==4:
        while True:
            base=float(input("enter the base of triangle"))
            heigth=float(input("enter the heigth of triangle"))
            area=0.5*base*heigth
            print("The area of triangle is", area)
            repeat=input("do you want to try again with sq?")
            if repeat=="no":
                break
    else:
        print("invalid input")
    repeat1=input("do you want to repeat again")
    if repeat1=="no":
        break