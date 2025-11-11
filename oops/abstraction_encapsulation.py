#*******************Abstraction*********************

#Abstraction is the mean of hiding the implementation of a class and only showing the essential features to the user.

#real life example:   a car internal feature not showing to the suer(driver),  driver only knows hwo to drive  he dont know how car internally works

class Car():
    def __init__(self):
        self.accelerater = False
        self.brake = False
        self.clutch = False
    
    def start(self):
        self.clutch = True   #un necessary fo user
        self.accelerater = True #unnecessary for user
        print("car started: ")   # necessary for user

car1 = Car()
car1.start()  

# in above example when we called function to start the car , car had startd, user only nedd the started car not the inner functionality, and we hided the unnecessry thing in class these wil not show to the user   this is abstraction


#**********************Encapsulation*************************

#Encapsulation is mean of wrapping data and function into a single unit (object)



#**********************practice questions*******************

#create account class withh 2 attributes - balance & account no. create methods for debit, credit and printing thhe balance.

class Account():
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, ammount):
          self.balance-=ammount
          print("The ammount Rs: ", ammount, "is debited from the accoutn! ", "new balance is Rs: ", self.get_balance() )

    def credit(self, ammount):
        self.balance+=ammount
        print("The ammount Rs: ", ammount, "is added in the accoutn! ", "new balance is Rs: ", self.get_balance())

    def get_balance(self):
        return self.balance
account1 = Account(800000, 8787878787878787)
print("User balance is: ", account1.balance, "and account number is: ", account1.account_no)
account1.debit(100000)
account1.credit(300000)