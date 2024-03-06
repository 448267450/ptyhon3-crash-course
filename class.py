class User:
    def __init__(self, name, email, age):
        self.name = name 
        self.email = email 
        self.age = age 
        
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age += 1


#Extend class
class Customer(User):
    #Constructor
    def __init__(self, name, email, age):
        super().__init__(name, email, age)
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# Init user object
ryan = User('Ryan Ren', 'ryan@gamil.com', 32)
ryan.has_birthday()

# Init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)
janet.set_balance(5000)


print(ryan.greeting())
print(janet.greeting())
        
