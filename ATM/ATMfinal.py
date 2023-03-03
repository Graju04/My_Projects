#ATMfinal.py ---- file name acts as module name
from ATMmenu import Menu
import sys
from ATMoperations import deposit,withdraw,balance_Enquiry
from ATMexceptions import DepositError,InsufficientFundError,WithdrawError
def atmproject():
    while(True):
        Menu()
        try:
            ch=int(input("Enter Your choice:"))
            match(ch):
                case 1:
                    try:
                        deposit()
                    except ValueError:
                        print("Don't Enter str, symbols and alpha-numerics for Deposit") 
                    except DepositError:
                        print("Don't enter -ve or zero amount for Deposit")
                case 2:
                    try:
                        withdraw()
                    except ValueError:
                        print("Don't enter str , symbols and alpha-numerics for withdraw")
                    except WithdrawError:
                        print("Don't enter -ve or zero amount for withdraw")
                    except InsufficientFundError:
                        print("Your Account does not have funds")
                case 3:
                      balance_Enquiry()
                case 4:
                      print("Thanks for using this program")
                      sys.exit() 
                case _:
                      print("your Selection of Operation is Wrong--Try Again!")
        except ValueError:
             print("\tDon't Enter strs,Symbols and alpha-numerics for the choice")              
                   


                    
