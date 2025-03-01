# wap to check a number is positive or not

# num=int(input("enter your number here"))
# if num>0:
#     print("num is positive")

# wap to check a num is even or odd
# num=int(input("enter your num here"))
# if num%2==0:
#     print("num is even")
# elif num%2!=0:
#     print("num is odd")
# else:
#     print(" enter a positive num")

# wap to create area calculator
# print("********Area claculator**************")
# print("""press 1 to get area of square
# press 2 to get area of rectangle
# press 3 to get area of circle
# press 4 to get area of triangle""")
# choice=int(input("enter a number between 1-4:"))
# if choice==1:
#     side =float(input("enter the length of one side"))
#     area=side*side
#     print("The area od square is ",area)
# elif choice==2:
#     length=float(input("enter the length of rect"))
#     breadth=float(input("enter the breadth of rect"))
#     area=length*breadth
#     print("The area of circle is",area)
# elif choice==3:
#     radius=float(input("enter the raduis of circle"))
#     area=(22/7)*radius**2
#     print("The area of circel is",area)
# elif choice==4:
#     base=float(input("enter the base of triangle"))
#     heigth=float(input("enter the heigth of triangle"))
#     area=0.5*base*heigth
#     print("The area of triangle is", area)
# else:
#     print("invalid input")

# wap check passed letter is vowel or not
# letter = input("enetr a letter here:")
# if letter in "aeiou" or letter in "AEIOU":
#     print("it is a vowel")
# else:
#     print("it is not a vowel")

# wap if a num is sigle double upto five digit
num=int(input("enter digit upto five digit"))
if num>=0 and num<=9:
    print("the num is single digit",num)
elif num>=10 and num<=99:
    print("the num is double digit",num)
elif num>=100 and num<=999:
    print("the num is triple digit",num)
elif num>=1000 and num<=9999:
    print("the num is four digit",num)
else:
    print("the num is five digit",num)