# generally in c++ or java language there is the concept of public and private in opps ,
# in python if we simply write the code for class as we see in other files practice, we can access  funtion and atrributed of a class to the outside of the class as below

class Bank_account():
    bank_name = "HBL"
    def __init__(self, accno, accpas):
        self.account_no = accno
        self.account_passward = accpas

    def show(self):
        print("account no: ", self.account_no, "account passward: ", self.account_passward, "has been saved in database" )

user1 = Bank_account("030303030303", "kiaKiaKia")  # we entered account no and passward
print(user1.bank_name, " Account No is: ", user1.account_no, " and Account passward is: ", user1.account_passward) # here we printed the account no and passward outside the class it means these functions and attributes are public
user1.show()   # here this function is also in the class and is public so we can access it outside,





# some times we have the tht needs to be hidden or private for making these attributes and functions private we use doubble underscore( __) with attribute or function to which we wana make private like example below:

class Bank_account2():  # class created for bnak 2
    bank_Name = "UBL" #  this is bank name that is public no matter bank name every one can see
    def __init__(self, accnoo, accpasw):
        self.__account_noo = accnoo  #  here we made this attribute private by adding __ before attribute
        self.__account_passwardd = accpasw  # same here we made this attribute private nwo we cannot access these attribute outside the class

    def __get(self):   # here we made this whole function private now this function will not exicute from outside the class
        print("account no: ", self.account_no, "account passward: ", self.account_passward, "has been saved in database" )
user2 = Bank_account2("8989898989898", "biabiabia")   # user entered account detail
# print(" Account No is: ", user1.account_noo, " and Account passward is: ", user1.account_passwardd) # here we tried to access data outsie teh class this will give error because this data is private
# user2.get()  # here this function accessing will also give error because it is private

print("bank name is : ",user2.bank_Name)  # but this attribute bank name is public to which we can access outside the class
