class Ticket:

    def __init__(self):
        self.Creator = input("What is your name? ")

        self.ID = input("What is your id? ")

        self.Email = input("What is your email? ")

        self.Issue = input("What is your issue? ").lower()

        self.Status = print("Not Yet Provided")


    print("hamburefer")

    def creator(self):
        if {self.Creator} != "":
            print(f"Name: {self.Creator}")

    def identify(self):
        print(f"Staff ID: {self.ID}")

    def email(self):
        print(f"Email Address: {self.Email}")

    def issue(self):
        print(f"Issue: {self.Issue}")

    def status(self):
        print(f"status: {self.Status}")
        if {self.Issue} == "change password".lower():
            password = (self.ID[0:2], self.Creator[0:3])
            newpassword = "".join(password)
            print(f"Description: Password changed to {newpassword}")



