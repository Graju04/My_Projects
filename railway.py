import sys
import random 



log_in = False
user_id = 0
pass_word = ''


class Train:
    def __init__(self,name = '', num = 0, arrival_time = '', departure_time = '', source = '', destination = '', day_Travel = '', seats_in_1AC = 0,seats_in_2AC = 0,seats_in_SL = 0, fare_of_1AC = 0, fare_of_2AC = 0, fare_of_SL = 0):
        self.name = name
        self.num = num
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.source = source
        self.destination = destination
        self.day_Travel = day_Travel
        self.seats = {'1AC' : seats_in_1AC, '2AC': seats_in_2AC, 'SL': seats_in_SL}
        self.fare = {'1AC' : fare_of_1AC, '2AC': fare_of_2AC, 'SL': fare_of_SL}

    def seat_available(self):
        print("Seats available in 1AC :- " +str(self.seats['1AC']))
        print("Seats available in 2AC :- " +str(self.seats['2AC']))
        print("Seats available in Sleeper(SL) :- " +str(self.seats['SL']))


    def check_availablity(self, coach = '',ticket_num = 0):
        coach = coach.upper()
        if coach not in ('SL','1AC','2AC'):
            self.seat_available()
            coach = input("Enter the coach(1AC/2AC/SL) :-")
        else:
            if self.seats[coach] == 0:
                return False
            elif self.seats[coach] >= ticket_num:
                return True
            else:
                return False     

    def book_tickets(self,coach = '',no_of_tickets = 0):
        self.seats[coach] -= no_of_tickets
        return True


class Tickets:
    def __init__(self,train,user,ticket_num,coach):
        self.PNR = str(train.num)+str(user.user_id)+str(random.randint(100,999))
        self.train_num = train.num
        self.coach = coach
        self.user_id = user.user_id
        self.train_name = train.name
        self.user_name = user.name
        self.ticket_num = ticket_num
        user.history.update({self.PNR : self})
        ticket_dict.update({self.PNR : self})


class user:
    def __init__(self,user_id = 0, name = '',hometown ='', phone_num = '', pass_word = ''):
        self.user_id = user_id
        self.name = name
        self.hometown = ''
        self.phone_num = ''
        self.pass_word = pass_word
        self.history = {}


class Acceptors:
    def accept_user_id():
        user_id = 0
        try:
            user_id = int(input("Enter User ID: "))
        except ValueError:
            print("Invalid User Id")
            return Acceptors.accept_user_id()
        else:
            return user_id

    def accept_pass_word():
        pass_word = input("Enter your password: ") 
        return pass_word

    def accept_train_number():
        train_num = 0
        try:
            train_num = int(input("Enter the Train Number: "))
        except ValueError:
            print("Please enter Train Number Properly!")
            return Acceptors.accept_train_number()
        else:
            if train_num not in trains:
                print("Please enter a valid Train Number")
                return Acceptors.accept_train_number()
            else:
                return train_num


    def accept_menu():
        option = input("Enter your option:")
        if option not in ('1','2','3','4','5','6','7','8'):
            print("Please enter a valid option!")
            return Acceptors.accept_menu()
        else:
            return int(option)


    def accept_coach():
        coach = input("Enter coach: ")
        coach = coach.upper()
        if coach not in ('SL','1AC','2AC'):
            print("Please enter coach properly!") 
            return Acceptors.accept_coach()
        else:
            return coach

    def accept_prompt():
        prompt = input("Confirm (yes/no): ") 
        if prompt not in ('y','n'):
            print("please enter valid option")
            return Acceptors.accept_prompt()
        return prompt

    def accept_ticket_num():
        ticket_num = 0
        try:
            ticket_num = int(input("Enter the number of tickets: "))
            if ticket_num < 0:
                raise ValueError
        except ValueError:
            print("Enter proper ticket number.") 
            return Acceptors.accept_ticket_num() 
        else:
            return ticket_num

    def accept_PNR():
        PNR = input("Enter your PNR number: ") 
        if PNR not in ticket_dict:
            print("Please enter proper PNR number: ")
            return Acceptors.accept_PNR() 
        else:
            return PNR

def book_ticket():
    if not log_in:
        login('p')
        
    check_seat_availablity('p')
    choice = Acceptors.accept_train_number()
    trains[choice].seat_available()
    coach = Acceptors.accept_coach()
    ticket_num = Acceptors.accept_ticket_num()
    if trains[choice].check_availablity(coach,ticket_num):
        print('You have to pay : ',trains[choice].fare[coach]*ticket_num,' ')
        prompt = Acceptors.accept_prompt()
        if prompt == 'y':
            trains[choice].book_tickets(coach,ticket_num)
            print("Booking Successful")
            tick = Tickets(trains[choice],users[user_id],ticket_num,coach)
            print("Please note PNR number :", tick.PNR)
            menu()
        else:
            print("Exit..") 
            menu()

    else:
        print(ticket_num," tickets not available")
        menu()


def  cancel_ticket():
        PNR = Acceptors.accept_PNR() 
        if PNR in ticket_dict:
            check_PNR(PNR)
            print("Cancel the tickets..?")
            prompt = Acceptors.accept_prompt()
            if prompt == 'y':
                if log_in:
                    print("Ticket Cancelled.\n")
                    trains[ticket_dict[PNR].train_num].seats[ticket_dict[PNR].coach] += ticket_dict[PNR].ticket_num
                    del users[ticket_dict[PNR].user_id].history[PNR]
                    del ticket_dict[PNR]
                else:
                    login('p')
                    print("Ticket Cancelled.\n")
                    trains[ticket_dict[PNR].train_num].seats[ticket_dict[PNR].coach] += ticket_dict[PNR].ticket_num
                    del users[ticket_dict[PNR].user_id].history[PNR]
                    del ticket_dict[PNR]
            # else:
            #     print("\nTicket not cancelled\n")
            # menu()




def check_seat_availablity(flag = ''):
    source = input("Enter the source station: ")
    destination = input("Enter the destination station: ")
    flag_2 = 0
    for i in trains:
        if trains[i].source == source and trains[i].destination == destination:
            print("Train Name: ", trains[i].name ," ","Number ", trains[i].num ," ","Day of Travel : ", trains[i].day_Travel)  
            flag_2 +=1
        if flag_2 == 0:    
            print("No Trains found between the station you entered.")
            menu()
        if flag == '':
            train_num = Acceptors.accept_train_number()
            trains[train_num].seat_available()
            menu()
        else:
            pass

 
            
def check_PNR(PNR = ''):
    if PNR == '':
        PNR = Acceptors.accept_PNR()
        print()
        print("User name:- ",ticket_dict[PNR].user_name)
        print("Train name:- ",ticket_dict[PNR].train_name)
        print("Train number:- ",ticket_dict[PNR].train_num," Source:- ",trains[ticket_dict[PNR].train_num].source," Destination:- ",trains[ticket_dict[PNR].train_num].destination)
        print("No. of Tickets Booked :- ",ticket_dict[PNR].ticket_num)
        print()
        menu()
    else:
        print()
        print("User name:- ",ticket_dict[PNR].user_name)
        print("Train name:- ",ticket_dict[PNR].train_name)
        print("Train number:- ",ticket_dict[PNR].train_num," Source:- ",trains[ticket_dict[PNR].train_num].source," Destination:- ",trains[ticket_dict[PNR].train_num].destination)
        print("No. of Tickets Booked :- ",ticket_dict[PNR].ticket_num)
        print()



def create_new_account():
    user_name = input("Enter your user name: ")
    pass_word = input("Enter your password:")
    user_id = random.randint(1000,9999)
    hometown = input("Enter your howetown: ")
    phone_number = input("Enter your phone number: ")
    U = user(user_id,user_name,hometown,phone_number,pass_word)
    print("Your User ID is : ", user_id)
    users.update({U.user_id : U})
    menu()

def login(flag = ''):
    global user_id
    global pass_word
    user_id = Acceptors.accept_user_id()
    pass_word = Acceptors.accept_pass_word()
    if user_id in users and users[user_id].pass_word == pass_word:
        print("\nWelcome ", users[user_id].name,"!\n")
        global log_in
        log_in = True
    else:
        print("\nNo such User ID found/ Invalid password!\n")
        return login()
    if flag == '':
        menu()
    else:
        pass
def check_previous_bookings():
    if not log_in:
        login('p')
    for i in users[user_id].history:
        print("\nPNR Number = ", i)
        check_PNR(i)
    menu()

def end():
    #s()
    print("------------------------------------Thank You--------------------------------")
    print("-----------------------------------------------------------------------------")
    sys.exit()




t1 = Train('odisha',12345,'12:34','22:12','ctc','kgp','Wed',30,23,43,2205,320,234)
t2 = Train('howrah',12565,'02:34','23:12','hwr','kol','Mon',33,4,12,3434,435,234)
t3 = Train('bangalore',22353,'11:56','03:12','ctc','ban','Fri',33,24,77,455,325,533)
trains = {t1.num:t1,t2.num:t2,t3.num:t3}
u1 = user(1111,'kiran','cuttack','7478021777','kiran')
u2 = user(2322,'alex parrish','new york','7873752967','alexparrish')
users={u1.user_id : u1, u2.user_id : u2}
ticket_dict = {}





print("--------Welcome to Railway Ticket Reservation Portal----------")
print("--------------------------------------------------------------")




def menu():
    print("<==========Choose one of the following option:- ==========>")
    print("<==================1.Book Tickets=========================>")
    print("<==================2.Cancel Tickets=======================>")
    print("<=============3.Check PassengerNameRecord=================>")
    print("<=============4.Check seat availablity====================>")
    print("<=============5.Create new account========================>")
    print("<=============6.Check previous bookings===================>")
    print("<=====================7.Login=============================>")
    print("<=====================8.Exit==============================>")
    func = { 1 : book_ticket, 2 : cancel_ticket, 3 : check_PNR, 4 : check_seat_availablity, 5 : create_new_account, 6 : check_previous_bookings, 7 : login, 8 : end}
    option = Acceptors.accept_menu()
    func[option]()

menu()    