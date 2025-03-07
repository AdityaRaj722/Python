# wap to find max of therr num
# def maximum_num(val1,val2,val3):
#     if val1>val2 and val3>val3:
#         print("the greatest value is:",val1)
#     elif val2>val1 and val2>val3:
#         print("the greatest value is:",val2)
#     else:
#         print("the greatest value is:",val3)
# maximum_num(4,7,5)


#  wap create ana print a list where the values are sq of num between 1 and 30
def list():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    return l
print(list())
# wap take num as a parameter and check the num is prime or not
def checkPrime(num):
    if num==1:print("it is not prime num")
    if num==2: print("it is a prime num")
    for i in range(2,11):
        if num%i==0:
            print("it is not a prime num")
            break
    else:
        print("it is a prime number")

checkPrime(10)
# wap sum all the numbers in the list
def add(number):
    total=0
    for i in number:
        total+=i
    return total
print(add([12,4,7,8,9,10]))

# using recursion
def addrec(numbers):
    if len(numbers)==1:
        return (numbers[0])
    else:
        return (numbers[0]+add(numbers[1:]))
print(addrec([12,4,7,8,9,10]))
# wap to solve fibonacci sequence using recursion

def fibonacci(n):
    if n==1:return 0
    if n==2:return 1
    return (fibonacci(n-1)+fibonacci(n-2))
print(fibonacci(7))

