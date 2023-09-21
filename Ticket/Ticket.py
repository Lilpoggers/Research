class Start:
    ticket_counter = 0

    #Uses inputs so the ticket has the info that is required.
    def __init__(self):
        Start.ticket_counter += 1
        self.Creator = input("What is your Name?: ")
        self.Staff = input("What is your ID?: ")
        self.Email = input("What is your Email Address?: ")
        self.Issue = input("What is your Issue?: ")
        self.response = None
        self.status = None

    #prints the ticket number, ticket creator, staff ID and the eamil address.
    def background1(self):
        print("")
        print("")
        print("Printing Tickets")
        print("")
        print(f"Ticket Number: {Start.ticket_counter}")
        print(f"Ticket Creator: {self.Creator}")
        print(f"Staff ID: {self.Staff}")
        print(f"Email Address: {self.Email}")

        #Makes it so if issues = change password or password change it closes the ticket and changes the description to the new password.
        if self.Issue.lower() in ["change password", "password change"]:
            newpassword = self.Staff[0:2] + self.Creator[0:3]
            print(f"Description: Password changed to {newpassword}")
            print(f"Response: New password generated: {newpassword}")
            self.status = "closed"
        else:
            print(f"Description: {self.Issue}")
            if self.response is None:
                print("Response: Not Yet Provided")
                self.status = "open"
            else:
                print(f"Response: {self.response}")
                self.status = "closed"


        print(f"Ticket Status: {self.status}")

    #Print the tickets statistics.
    def background2(self):
        print("")
        print("")
        print("Displaying Ticket Statistics")
        print("")
        #Prints how many tickets have been resolved.
        print(f"Tickets Created: {Start.ticket_counter}")
        if self.status == "closed":
            resolved = 1
        else:
            resolved = 0
        print(f"Tickets Resolved: {resolved}")
        #Prints how many tickets have been solvec.
        if self.status == "open":
            solve = 1
        else:
            solve = 0
        print(f"Tickets To Solve: {solve}")