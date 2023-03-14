customerNames = ['RaviKishore', 'Venkatesh', 'David', 'CMR', 'Will Smith']
customerPins = ['1234','5678','7890','4321','6543']
AccountBalance = [10000,20000,30000,40000,50000]
Deposit = 0
Withdraw = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0


while True:
    print("============================================")
    print("-----Welcome to Union Bank of India---------")
    print("-------1. Open a new Account----------------")
    print("-------2. Withdraw Money--------------------")
    print("-------3. Deposit Money---------------------")
    print("-------4. Check customers & Balance---------")
    print("--------------5. Exit-----------------------")

    option = input("Select your choice:")  
    if option == "1":
        print("Option 1(create a new account) is selected")
        noc = eval(input("Number of customers:"))
        i = i + noc
        if i > 5 :
            print("\n")
            print("Customer registration exceed reached")
            i = i - noc
        else:

            while counter_1 <= i:
                Name = input("Enter your name:")
                customerNames.append(Name)
                pin = str(input("Enter 4 digit pin of your choice:"))
                customerPins.append(pin)
                balance = 0
                Deposit = eval(input("Enter amount you want to deposit:"))
                balance += Deposit
                AccountBalance.append(balance)
                #if counter_2 < i:       # if counter_2 < len(customerNames):
                print("\nName=", end=" ")
                print(customerNames[counter_2])
                print("Pin=", end=" ")
                print(customerPins[counter_2])
                print("Balance=", end=" ")
                print(AccountBalance[counter_2], end=" ")
                print("-/Rs")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                
                print("\nYour name is added to customers system")
                print("Your pin is added to customer system")
                print("Your balance is added to customer system")
                print("----New account created successfully !----")
                print("\n")
                print("Your name is avalilable on the customers list now : ")
                print(customerNames)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("========================================")

        Menu = input("Press enter key for main Menu")   
    elif option == "2":
        j = 0
        print("Option 2(Withdraw money) is selected")
        while j < 1:
            k = -1
            name = input("Please input name:")
            pin  = input("Please input pin:")

            while k < len(customerNames) -1:
                k = k + 1

                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1

                        print("Your current Balance:",end=" ")
                        print(AccountBalance[k],end=" ")
                        print("/Rs\n")
                        balance = (AccountBalance[k])
                        withdraw = eval(input("Enter amount to withdraw:"))

                        if withdraw > balance:
                            Deposit = eval(input("please deposit a  higher amount because the balance mentioned above is not enough:"))
                            balance = balance + Deposit
                            print("Your Current Balance:",end=" ")
                            print(balance,end=" ")
                            print("/Rs\n\n")
                            print("Withdraw Successfull!")
                            AccountBalance[k] = balance
                            print("your New Balance:",balance,end=" ")
                            print("/Rs\n\n")
                        else:

                            balance = balance - withdraw
                            print("\n")
                            print("----Withdraw Successfull!----")
                            AccountBalance[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")    
            if j < 1:
                print("Your name and pin does not match!\n")
                break
        Menu = input("Press enter key for main Menu") 
    elif option == "3":
        print("option 3 (Deposit Money) is selected")
        n = 0

        while n < 1:
            k = -1
            name = input("Enter your name:")
            pin = input("Enter your pin:") 

            while k < len(customerNames) -1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1


                        print("Your Current Balance: ", end=" ")
                        print(AccountBalance[k], end=" ")
                        print("-/Rs")
                        balance = (AccountBalance[k])
                        # This statement below takes the depositionn from the customer.
                        deposition = eval(input("Enter the value you want to deposit : "))
                        balance = balance + deposition # 1000+500=1500
                        AccountBalance[k] = balance
                        print("\n")
                        print("----Deposit successful!----")
                        print("Your New Balance: ", balance, end=" ")
                        print("-/Rs\n\n")   
            if n < 1:
                print("Your name and pin does not match")
                break
        Menu = input("Press enter key for main Menu")  
    elif option == "4":
        print("option 4 (customer list & Balance) is selected")
        k = 0
        print("customers list and Balance ") 
        print("\n")
        while k <= len(customerNames) -1:
            print("->.Customer =", customerNames[k])
            print("->.Balance =", AccountBalance[k], end=" ")
            print("-/Rs")
            print("\n") 
            k = k + 1
        Menu = input("Press enter key for main Menu") 
    elif option == "5":
        print("Choice number 5(Exit) is selected by the customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Visit Again")
        break
    else:
        # This else function above would work when a wrong function is chosen.
        print("Invalid option selected by the customer")
        print("Please Try again!")
        # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")




