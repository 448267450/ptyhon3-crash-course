def sayHello(name='Sam'):
    print(f'Hello {name}')

# sayHello('Ryan Ren')
# 
    
def getSum(num1, num2):
    total = num1 + num2
    return total


# print(getSum(3, 4))

getSum = lambda num1, num2: num1 + num2
print(getSum(11, 23))

