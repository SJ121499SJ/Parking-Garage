class Parking_garage():
    price = 5
    # initialize class
    def __init__(self,):
        self.tickets = []
        self.parking_spaces = sorted(['a1','a2','a3','a4','a5','a6','a7'])
        self.current_tickets = {'a1':{'Paid':True},
                                'a2':{'Paid':True},
                                'a3':{'Paid':True},
                                'a4':{'Paid':True},
                                'a5':{'Paid':True},
                                'a6':{'Paid':True},
                                'a7':{'Paid':True}}
                               
    
    def takeTicket(self):
        print (self.parking_spaces)
        while self.parking_spaces == []:
            print("Sorry, there are no more spaces available")
            self.runner()
        
        user_spot_choice = (input("What spot would you like (Type 'q' to quit) ")).lower()
        
        while True:
            if user_spot_choice in self.parking_spaces:
                self.parking_spaces.remove(user_spot_choice)
                self.tickets.append(user_spot_choice)
                print (f"Your choice of {user_spot_choice} has been selected. Please take your ticket")
                self.current_tickets[user_spot_choice]['Paid'] = False
                print (self.parking_spaces)
                print(self.tickets)
                print(self.current_tickets)
        
            elif user_spot_choice == 'q':
                break
            
            else:
                print (f"Your choice of {user_spot_choice} is not available. Please choose another spot")

        
            

    def payForParking(self):
        price = 5
        user_choice_for_payment = input("What was your parking spot? (a1 ~ a7) (type 'q' to quit) ")
        while price > 0:
            payment = int(input("Please pay $" + str(price) + " for your parking spot "))
            
            if payment < price:
                print ("Your payment is short " + str(price-payment)+ " dollars")
                price -= payment
            elif payment == price:
                self.current_tickets[user_choice_for_payment]['Paid'] = True
                self.parking_spaces.append(user_choice_for_payment)
                self.tickets.remove(user_choice_for_payment)
                print(sorted(self.parking_spaces))
                print(sorted(self.tickets))
                print(self.current_tickets)
                self.leaveGarage()
                break
            elif payment > price:
                print ("Your change is " + str(payment - price)+ " dollars")
                self.current_tickets[user_choice_for_payment]['Paid'] = True
                self.parking_spaces.append(user_choice_for_payment)
                self.tickets.remove(user_choice_for_payment)
                print(sorted(self.parking_spaces))
                print(sorted(self.tickets))
                print(self.current_tickets)
                self.leaveGarage()
                break
            elif user_choice_for_payment == 'q':
                break
        
        

    def leaveGarage(self):
        print("Thank you, Have a nice day! Please leave in 15 minutes")
    
    def runner(self):
        while True:
            user_choice = (input("What would you like to do (Pay Ticket or Get a spot) (Type 'q' to quit) ")).lower()
            if user_choice == 'pay ticket':
                self.payForParking()
                
            elif user_choice == 'get a spot':
                self.takeTicket()

            elif user_choice == 'q':
                break



test = Parking_garage()
test.runner()







