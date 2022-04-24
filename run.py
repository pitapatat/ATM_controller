import atm
from atm import NotAvailableError, Account, Card, ATM_controller


# behavior function for user 
def user_func(insert_card):
    # insert card
    atm = ATM_controller(insert_card)
    # enter your PIN number(6 digits)
    PIN = input("please enter your PIN number")   #PIN = 221958
    try:
        connection = atm.check_PIN(int(PIN))
    except: 
        print(f"you are wrong! you entered {PIN}. please check your PIN number again")
        user_func(card)
        
    # after checking PIN number, choose the bank  
    while connection == True:
        #print(connection)
        account = Account(RRN)
        bank_name = input("please enter bank name(eg. KB, WOORI, SH, etc)")  #bankname = 'KB'      
        connection_2 = atm.check_account(bank_name, account, connection)
        #print(connection_2)
        
        # after connecting the bank account, choose what you want to do
        while connection_2 == True:
            print("you can enter the number for your work") 
            print("number 1 is for checking the balance, 2 is for deposit, 3 is for withdrawal")
            num = input("what do you want to do ? please enter the number")
            
            # check the balance
            if num == '1':
                atm.current_balance()
            
            # deposit the money
            elif num == '2':
                money = input("how much do you want?") # money
                atm.deposit(int(money))
            
            # withdraw the money
            elif num == '3':
                money = input("how much do you want?") # money
                try:
                    atm.withdraw(int(money))
                except:
                    current_balance = atm.current_balance()
                    print(f"you are not allowed to withdraw. {current_balance}")
                    continue
            else:
                print("do you want to exit the program?")
                time.sleep(3)
                sys.exit('program exit. bye!')
        else: 
            print("please choose annother bank account")    
    
    else:
        user_func(card)
    


###############################
RRN = '123456'
name  = 'hani'
phone_number  = '010-1234-5678'
bank = 'KB'
################################


if __name__ == '__main__':

    account = Account(RRN)
    account.deposit(5000)

    card = Card(RRN, name,phone_number)
    # user func 실행
    user_func(card)
    
