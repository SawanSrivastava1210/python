# Exercise 7.3
# Create a class Account which works like a bank  
# Sawan Srivastava
# 1/15/2020
class Account:
    def __init__(self, user_id = 0, balance = 100, annualInterestRate = 0):
            self.__user_id = user_id
            self.__balance = balance
            self.__annualInterestRate = annualInterestRate
            
    def set_id (self, user_id):
        self.__user_id = user_id
             
    def set_balance (self, balance):
        self.__balance = balance

    def set_annualInterestRate (self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def get_id(self):
        return self.__user_id

    def get_balance(self):
        return self.__balance

    def get_annualInterestRate(self):
        return self.__annualInterestRate

    def getMonthlyInterest(self):
        return self.__annualInterestRate/12 * self.__balance

    def withdraw(self, withdrawAmount):
        self.__balance = self.__balance - withdrawAmount
        print('Your balance is now', self.__balance)

    def deposit(self, depositAmount):
        self.__balance = self.__balance + depositAmount
        print('Your balance is now', self.__balance)

Person1 = Account(1122, 20000, 0.045)
Person1.withdraw(2500)
Person1.deposit(3000)
print('Your id is', Person1.get_id())
print('Your balance is $'+ str(Person1.get_balance()))
print('Your monthly interest rate is', Person1.get_annualInterestRate()/12)
print('Your monthly interest is $'+ str(Person1.getMonthlyInterest()))
print(Person1.getMonthlyInterest())
        
        
        
        
        
        

     
         
