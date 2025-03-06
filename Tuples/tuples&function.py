a=("OnePlus","Nokia","Redmi")

print(a.count("Redmi"))
print(a.index("Nokia"))
a=list(a) #tuple to list conversion
print(type(a))
a.append("Mi")
a=tuple(a)
print(a)
print(type(a))