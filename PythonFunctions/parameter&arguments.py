def add(x,y):  #parameter are passed
    print(x+y)
add(5,7)  # provided values are called argumnets

def rect(length,width):
    print("Area is:",length*width)
rect(4,8)

# arbitary argumnets
def hello(*name):
    print("My name is :", name[1])
hello("Adi","Sam","Lisa")