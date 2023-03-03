#ATMoperations.py  ---- file name acts as Module name
from ATMexceptions import DepositError,InsufficientFundError,WithdrawError
bal=500.00    #global variable
def deposit():
    deposit_amount=float(input("Enter the deposit amount:"))       # Raising valueerror implicitly
    if (deposit_amount<=0):
        raise DepositError     #raise Depositerror Explicitly
    else:
        global bal
        bal=bal+deposit_amount
        print("Your Account number XXXXXXX2345 Credited with INR:{}".format(deposit_amount))
        print("Now Your Current Balance:{}".format(bal))
def withdraw():
    global bal
    withdraw_amount = float(input("Enter the amount You want to withdraw:"))              # Raising ValueError implicitly
    if(withdraw_amount<=0):
        raise WithdrawError  # Raising WithdrawError Explicitly
    elif((withdraw_amount+500)>bal):
        raise InsufficientFundError  # Raising InSuffundError Explicitly
    else:
        bal=bal-withdraw_amount
        print("Ur Account XXXXXX123  debited with INR:{}".format(withdraw_amount))
        print("Now Ur Current Bal :{}".format(bal))

def balance_Enquiry():
    print("Your Account Balance:{}".format(bal))        
