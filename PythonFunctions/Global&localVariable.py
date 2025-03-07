# local variavble
# x=24
# print(x)
# def hello():
#     x=25
#     return x
# print(hello())
# print(x)

# global variable
x=24
print(x)
def hello():
    global x
    x=25
    return x
print(hello())
print(x)
