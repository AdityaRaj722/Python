# def hello():
#     return ("hello world")
# print(hello())
#
# def add(a,b):
#     return a+b
# print(add(12,45))

# def hello():
#     print("hello")
#     return hello()
# print(hello())

def factorial(a):
    if a==1: return 1
    return a*factorial(a-1)
print(factorial(5))
