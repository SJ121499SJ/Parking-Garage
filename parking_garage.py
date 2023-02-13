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
                               
    # method for when user takes a ticket
    def takeTicket(self):
        # shows available parking spaces
        print (self.parking_spaces)
        # looks for if there are no more parking spaces available
        while self.parking_spaces == []:
            print("Sorry, there are no more spaces available")
            self.runner()
        
        # asks what spot the user would like to park in
        user_spot_choice = (input("What spot would you like (Type 'q' to quit) ")).lower()
        
        while True:
            if user_spot_choice in self.parking_spaces:
                # when user chooses a spot, it removes that spot from the list of available parking spaces
                self.parking_spaces.remove(user_spot_choice)
                # puts parking space into tickets list
                self.tickets.append(user_spot_choice)
                print (f"Your choice of {user_spot_choice} has been selected. Please take your ticket")
                # changes boolean from current_tickets in space user selected to false, showing they haven't paid their ticket yet
                self.current_tickets[user_spot_choice]['Paid'] = False
                # next three print statements shows and verifies what has been done when user took a ticket
                print (self.parking_spaces)
                print(self.tickets)
                print(self.current_tickets)
        
            # user can type 'q' to quit out 
            elif user_spot_choice == 'q':
                break
            # recognizes if user's choice of parking spot has already been taken
            else:
                print (f"Your choice of {user_spot_choice} is not available. Please choose another spot")

        
            
    # method to pay for parking space
    def payForParking(self):
        # set a variable that shows price of ticket
        price = 5
        # asks user what spot they parked in
        user_choice_for_payment = input("What was your parking spot? (a1 ~ a7) (type 'q' to quit) ")
        # tells user to pay 'price' for their spot
        while price > 0:
            payment = int(input("Please pay $" + str(price) + " for your parking spot "))
            
            # if user pays less than the current price, tells user they are short a certain amount of dollars
            if payment < price:
                print ("Your payment is short " + str(price-payment)+ " dollars")
                price -= payment
            # shows user paid price in full, updates lists and dictionary
            elif payment == price:
                self.current_tickets[user_choice_for_payment]['Paid'] = True
                self.parking_spaces.append(user_choice_for_payment)
                self.tickets.remove(user_choice_for_payment)
                print(sorted(self.parking_spaces))
                print(sorted(self.tickets))
                print(self.current_tickets)
                self.leaveGarage()
                break
            # recognizes if user paid more, gives change depending on how much they paid, also updates lists and dictionaries
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
            # user can type 'q' to quit
            elif user_choice_for_payment == 'q':
                break
        
    # method to leave garage
    def leaveGarage(self):
        # thanks them for coming after paying, asks them to leave in 15 minutes
        print("Thank you, Have a nice day! Please leave in 15 minutes")
    
    # runner method to keep inputs running for people coming and going in parking garage
    def runner(self):
        while True:
            # asks user what they want to do, pay ticket, get a spot, or quit
            user_choice = (input("What would you like to do (Pay Ticket or Get a spot) (Type 'q' to quit) ")).lower()
            # if user types pay ticket, it runs the payForParking method
            if user_choice == 'pay ticket':
                self.payForParking()
            # if user types get a spot, it runs the takeTicket method
            elif user_choice == 'get a spot':
                self.takeTicket()
            # user can type 'q' to quit
            elif user_choice == 'q':
                break



test = Parking_garage()
test.runner()







