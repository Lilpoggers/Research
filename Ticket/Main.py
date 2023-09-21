from Ticket import Start

def main():
    #Asks how many tickets that want to be made.
    n = int(input("How many tickets do you want to create: "))
    mylist = []

    #Uses list and range to make the ticket sthat were stated.
    for i in range(n):
        newticket = Start()
        mylist.append(newticket)
    print("Tickets Created:", len(mylist))

    #Asks if you want to print all the tickets that were made.
    last_plane = input("Do you want to print all tickets? Yes or No? ").lower()
    if last_plane == "yes":
        for ticket in mylist:
            ticket.background1()
            
    #Asks if you want to print all the statistics that were made.
    bike = input("Do you want to see the statistics? Yes or No? ").lower()
    if bike == "yes":
        for ticket in mylist:
            ticket.background2()

if __name__ == "__main__":
    main()