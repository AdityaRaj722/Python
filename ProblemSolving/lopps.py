# wap to find sum all the even num upto 50
# a = 0
# for i in range (1, 51):
#     if i % 2 == 0:
#         a += i
#
#
# print(a)

# wap write first 20num and their square
# for i in range(1,21):
#     print(i," = ",i**2)

# wap first 10 odd number using while loop
# sum=0;
# i=0;
# while(i<=20):
#     if i%2!=0:
#         sum+=i
#     i+=1
# print(sum)

# wap check if num divisible by 8 and 12 upto 100
# for i in range (101):
#     if i%8==0 and i%12==0:
#         print(i)

# wap create a billing system at supermarket
while True:
    name=input("enter customer name:")
    total=0

    while True:
        print("enter the amount and quantity")
        amount=float(input("enter amount"))
        quantity=float(input("enter quantity"))
        total+=amount*quantity
        repeat=input('do you want to add more items? (yes/no):')
        if repeat =='no' or repeat=='NO':
            break
    print("-"*40)
    print("Name:" ,name)
    print("Amount to be paid: ",total)
    print("-"*40)
    print("*********Happy Shopping***********")

    repeat1=input("do you want to go to next customer? (yes/no):")
    if repeat1=="no" or repeat1=="NO":
        break