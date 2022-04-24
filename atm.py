import random
import numpy as np
import sys

######

# Account : 
# Card :
# ATM_controller :

######


class NotAvailableError(Exception):
    pass



class Account():
    # suppose 1) bank name 'KB' 2) if you want to open an account, you need a RRN(Resident Registration Number)
    def __init__(self,RRN:int, bank_name = 'KB', balance = 0):
        
        np.random.seed(42)

        self.RRN = RRN 
        self.bank_name = bank_name
        self.__account = str(np.random.randint(1000000, 999999999)).zfill(10)  # open an account!(10 digits)
        self.balance = balance
        
    # check the balance
    def current_balance(self):
        print(f"your current balance is {self.balance}")
        return self.balance

    # make a deposit 
    def deposit(self, cash:int):
        if type(cash) == int:
            self.balance += cash
            print(f"you have deposited {cash}. your current balance is {self.balance}")
        else: 
            raise NotAvailableError('you have to enter the "interger". please check it again!')
        return self.balance
    
    # withdraw money
    def withdrawal(self, cash:int):
        if type(cash) == int :
           
            if self. balance < cash :
                raise NotAvailableError(f'you are not allowed to withdraw more than {self.balance}')
            else :
                self.balance -= cash
                print(f"successed! balance = {self.balance}")
            
        else: 
            raise NotAvailableError('you have to enter the "interger". please check it again!')
        return self.balance




class Card():
    # suppose to issue a credit card, you need RRN, name, phone_number   
    def __init__(self, RRN:int, name:str, phone_number):
        np.random.seed(42)
        self.RRN = RRN 
        self.name = name
        self.phone_number = phone_number
        self.__PIN = np.random.randint(100000,999999)  # got a PIN number 
        self.account = None
        
        

class ATM_controller():
    # to use ATM, you should insert the card
    def __init__(self, card, connect=False):
        self.card = Card(RRN, name, phone_number)
        self.connect = connect
        #print("your cart inserted!")
        
    # first of all, check the PIN number 
    def check_PIN(self, PIN):
        self.connect = False
        self.__PIN = PIN
        # if the PIN number is correct, connection is succesful
        if self.__PIN == self.card._Card__PIN:
            print("connected!")
            self.connect = True
        else:
            raise NotAvailableError("you are wrong! please enter your PIN number")
        return self.connect 


    # select the account 
    def check_account(self, bank, account, connection=False):
        # account = Account(RNN), connection = check_PIN(PIN)
        self.connect = connection
        if self.connect == True: 
            if account._Account__account:
                if account.bank_name == bank:
                    self.account = account._Account__account
                    print(f"your account is connected. account_number : {self.account}")
                    self.connect = True

                else:
                    print("please enter annother bank name")
                    self.connect = False
                    
        else: 
            self.connect = False
            raise NotAvailableError("it's wrong path. your PIN number is not corrected")
        return self.connect

        
    def current_balance(self):  
        if self.connect == True:
            account.current_balance()

    def deposit(self, number):
        if self.connect == True:
            account.deposit(number)            
             

    def withdraw(self, number): 
        if self.connect == True:
            account.withdrawal(number)
            


