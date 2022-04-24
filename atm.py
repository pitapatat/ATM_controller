import random
import numpy as np
import sys


class NotAvailableError(Exception):
    pass

#IF KB
class Account():

    def __init__(self,RRN:int, bank_name = 'KB', balance = 0):
        np.random.seed(42)

        self.RRN = RRN 
        self.bank_name = bank_name
        self.__account = str(np.random.randint(1000000, 999999999)).zfill(10)
        self.balance = balance
        
        

    def current_balance(self):
        print(f"your account is opened. balance = {self.balance}")
        return self.balance

    
    def deposit(self, cash:int):
        if type(cash) == int:
            self.balance += cash
            print(f"balance = {self.balance}")
        else: 
            raise NotAvailableError('you should int')
        return self.balance
    


    def withdraw(self, cash:int):
        if type(cash) == int :
            
            if self. balance < cash :
                raise NotAvailableError(f'you cannot withdraw your cash. your balance : {self.balance}')
            else :
                self.balance -= cash
                print(f"successed! balance = {self.balance}")
            
        else: 
            raise NotAvailableError("please 00 dollar")
        return self.balance




class Card():

    # 카드 만들때 필요 정보
    def __init__(self, RRN:int, name:str, phone_number):
        np.random.seed(42)
        self.RRN = RRN 
        self.name = name
        self.phone_number = phone_number
        self.__PIN = np.random.randint(100000,999999)
        self.account = None
        #print("your card info is registered")
        
        

class ATM_controller():
    def __init__(self, card, connect=False):
        self.card = Card(RRN, name, phone_number)
        self.connect = connect
        #super().__init__(self, Account)
        #print("your cart inserted!")
        

    def check_PIN(self, PIN):
        self.connect = False
        self.__PIN = PIN
        if self.__PIN == self.card._Card__PIN:
            print("connected!")
            self.connect = True
            return self.connect 
        else:
            #raise NotAvailableError
            print("you are wrong! please enter your PIN number")
            self.connect = False
            return self.connect 


    # 계좌 연결(계좌 있으면 은행 선택해서 그걸로 연결)
    def check_account(self, bank, account, connection=False):
        ## account = Account()
        self.connect = connection
        if self.connect == True: 
            if account._Account__account:
                try:
                    if account.bank_name == bank:
                        self.account = account._Account__account
                        print(f"your account connected. {self.account}")
                        self.connect = True
                        return self.connect 
                    else:
                        print("please choose annother bank account")
                        self.connect = False
                        return self.connect 

                except:
                    print("you dont have account")
                    self.connect = False
                    return self.connect 

        else: 
            self.connect = False
            return self.connect
            #raise NotAvailableError("please connecting your PIN number. it's wrong path")


        
    def current_balance(self):  
        if self.connect == True:
            account.current_balance()

    def deposit(self, number):
        if self.connect == True:
            account.deposit(number)            
            #super().deposit(number)   

    def withdraw(self, number): 
        if self.connect == True:
            account.withdraw(number)
            #super().withdraw(number)



#####
RRN = '123456'
name  = 'hani'
phone_number  = '010-1234-5678'
bank = 'KB'




# card insert
def user_func(insert):
    atm = ATM_controller(insert)
    PIN = input("for checking your identity. please enter our PIN number")  #PIN=input()
    #PIN = 221958
    connection = atm.check_PIN(int(PIN))
    # 계좌 생성자 
    while connection == True:
        print(connection)
        account = Account(RRN)
        bank_name = input("choose youe bank name")
        #bank = 'KB'
        # 계좌 연결
        connected_2 = atm.check_account(bank_name, account, connection)
        print(connected_2)
        
        while connected_2 == True:
            num = input("what do you want? YOU CANT CHOOSE 1,2,3")
            if num == '1':
                print(atm.current_balance())
            elif num == '2':
                money = input(" how much ?") # money
                atm.deposit(int(money))

            elif num == '3':
                money = input(" how much ?") # money
                try:
                    atm.withdraw(int(money))
                except:
                    BAL = atm.current_balance()
                    print(f"you cant wuthdraw your money. you have:{BAL}")
                    continue
            else:
                sys.exit('programe bye')
        else: 
            print("please choose annother bank account")

    
    
    else:
        user_func(card)
    

    #num = input("what do you want more?")









