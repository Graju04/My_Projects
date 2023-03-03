from ATMfinal import atmproject
import getpass,sys
def atmproject_run():
    attempts=1
    while(True):
        pass_word=input("Enter Your Password:")
        if (pass_word=="python"):
            atmproject()
        else:
            if(attempts==3):
                print("Dear customer Invalid credentials")
                sys.exit()
            attempts=attempts+1

#main program
atmproject_run()                    