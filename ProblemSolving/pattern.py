# triangle pattern
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# output
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# **************************
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
#
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# *******************************************

# for i in range(1,6):
#     for j in range(i,6):
#         print(i,end=" ")
#     print()
# output
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
#*********************************************
# for i in range(1,6):
#     for j in range(i,6):
#         print("",end=" ")
#     for k in range (i):
#         print("x",end="")
#     print()
#
#     x
#    xx
#   xxx
#  xxxx
# xxxxx
# ******************************************
# a=0
# for i in range(1,6):
#     a=i
#     for j in range(1,i+1):
#         print(a,end=" ")
#         a-=1
#     print()
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# ***********************************

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for k in range(5,0,-1):
#     for j in range(0,k-1):
#         print("*",end=" ")
#     print()
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# ******************

for i in range (1,11):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()