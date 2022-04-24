import atm
from atm import NotAvailableError, Account, Card, ATM_controller

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




if __name__ == '__main__':
    #print("hello!")
    print("please insert your card info")


    account = Account(RRN)
    account.deposit(5000)

    card = Card(RRN, name,phone_number)
    # user func 실행
    user_func(card)
    #print(card._Card__PIN)
    
