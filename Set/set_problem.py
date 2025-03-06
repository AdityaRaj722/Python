# wap to find min and max in set
a={12,4,7,5,4,8,9,3,}
min=min(a)
max=max(a)
print("min value in set is",min)
print("max value in set is",max)
# wap find comman elelments ih three list using set
a=[1,5,4,7,6]
b=[4,5,6,7]
c=[4,7,8,5,2,1]
print(set(a)&set(b)&set(c))
# wap to find defference between two sets
a={1,5,4,7,6}
b={4,5,6,7}
print(a.difference(b))
# wap to remove an item from a set if it is present in the list
a.discard(5)
print(a)

#  wap to check if a set is a subset another set
d={1,4,6}
print(d.issubset(a))