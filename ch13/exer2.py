class User():
    def __init__(self, firstname, lastname, age, address, birthday):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.address = address
        self.birthday = birthday
        self.login = 0
        
    def Describe_User(self):
        print(self.firstname+" "+self.lastname)
        print(self.age)
        print(self.address)
        print(self.birthday)
    
    def greet_use(self):
        print("\nHello there " +self.firstname)
        
    def increment_login_attempts(self):
        self.login += 1
    
    def reset_login_attempts(self):
        self.login = 0
        
Benjo = User('Benjo','Kalaw','25','Plaridel Lipa City','November 7 1996')
Benjo.Describe_User()
Benjo.greet_use()
x = 1

print('Attempting to login 5x')
while x<=5:
    Benjo.increment_login_attempts()
    x +=1
print('\nWe have tried logging you in '+ str(Benjo.login)+' times')

print('\nresetting login attempts')
Benjo.reset_login_attempts()
print('Current login attempts: '+ str(Benjo.login))
    