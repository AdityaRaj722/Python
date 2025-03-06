# a={"Ironman","Hulk","Thor","Captain America"}
# add
# a.add("Spiderman")
# print(a)

# pop
# a.pop()
# a.remove("Thor")
# print(a)

# discard
# a.discard("Hulk")
# print(a)

# copy
# b=a.copy()
# print(b)

a={"Ironman","Hulk","Thor","Captain America"}
b={"Supermna","Batman","Wonder-women"}
c={"Hulk","Thor"}

# disjoint
print(a.isdisjoint(c))

# issubset
print(c.issubset(a))

# superset
print(a.issuperset(c))

# update
a.update(b)
print(a)

# clear
a.clear()
print(a)