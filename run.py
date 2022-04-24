import time
import sys
import atm
from atm import NotAvailableError, RejectionError, Account, Card, ATM_controller


# behavior function for user 
def user_func(insert_card):
    # insert card
    atm = ATM_controller(insert_card)
    # enter your PIN number(6 digits)
    PIN = input("please enter your PIN number")   #PIN = 221958
    print(" "*30)
    try:
        connection = atm.check_PIN(int(PIN))
    except: 
        print(f"you are wrong! you entered {PIN}. please check your PIN number again!")
        print(" "*30)
        user_func(card)
        
    # after checking PIN number, choose the bank  
    while connection == True:
        #print(connection)
        #account = Account(RRN)
        bank_name = input("please enter bank name(eg. KB, WOORI, SH, etc)")  #bankname = 'KB'      
        print(" "*30)
        connection_2 = atm.check_account(bank_name, account, connection)
        #print(connection_2)
        
        # after connecting the bank account, choose what you want to do
        while connection_2 == True:
            print(" "*30)
            print("****"*10)
            print("what can i do for you? please choose the number")
            print("\t1:checking the balance, 2:deposit, 3:withdrawal")
            print("****"*10)
            print(" "*30)
            num = input("what do you want to do ? please enter the number")
            print(" "*30)
            
            # check the balance
            if num == '1':
                atm.current_balance(account)
            
            # deposit the money
            elif num == '2':
                money = input("how much do you want to deposit?") # money
                print(" "*30)
                try:
                    atm.deposit(account, int(money))
                except:
                    print(f"you have to enter the 'interger'")
                    print(" "*30)
                    continue

            
            # withdraw the money
            elif num == '3':
                money = input("how much do you want to withdraw?") # money
                print(" "*30)
                try:
                    atm.withdraw(account, int(money))
                except ValueError:
                    print(f"you have to enter the 'interger'")
                    print(" "*30)
                    continue

                except RejectionError:
                    current_balance = atm.current_balance(account)
                    print(f"you are not allowed to withdraw. {current_balance}")
                    print(" "*30)
                    continue

            else:
                time.sleep(1)
                sys.exit('bye!')

    else:
        user_func(card)
    

############################################
RRN = '123456'
name  = 'hani'
phone_number  = '010-1234-5678'
bank = 'KB'
############################################

account = Account(RRN)
account.deposit(int(50000))
card = Card(RRN, name,phone_number)

if __name__ == '__main__':
    user_func(card)
