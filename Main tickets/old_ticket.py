class Tickets:
    while True:

        Creator = input(f"What is your Name?: ")
        Staff = input(f"What is your ID?: ")
        Email = input(f"What is your Email Address?: ")
        Issue = input(f"What is your Issue?: ")

        response = ""
        ticket = ""
        status = ""

        print("")
        print("")
        print("Printing Tickets")
        print("")

        if Creator != (""):
            number = (2000)
            number += 1
            print(f"Ticket Number: {number}")

        print(f"Ticket Creator: {Creator}")

        print(f"Staff ID: {Staff}")

        print(f"Email Address: {Email}")

        if Issue == ("change password").lower():
            password = (Staff[0:2], Creator[0:3])
            newpassword = "".join(password)
            print(f"Description: Password changed to {newpassword}")

        elif Issue == ("password change").lower():
            password = (Staff[0:2], Creator[0:3])
            newpassword = "".join(password)
            print(f"Description: Password changed to {newpassword}")

        else:
            print(f"Description: {Issue}")

        if Issue == ("change password").lower():
            print(f"Response: New password generated: {newpassword}")

        elif response == "":
            print("Response: Not Yet Provided")

        else:
            print(f"Response: {response}")

        if Issue == ("change password").lower():
            status = "closed"

        elif Issue == ("password change").lower():
            status = "closed"

        elif response == "":
            status = "open"

        else:
            status = "closed"

        if status == "closed":
            print(f"Ticket Status: Closed")
        else:
            print(f"Ticket Status: Open")

        print("")
        print("")
        print("Displaying Ticket Statistics")
        print("")

        created = 0
        created += 1
        print(f"Tickets Created: {created}")

        if status == "closed":
            resolved = 0
            resolved += 1
            print(f"Tickets Resolved: {resolved}")
        else:
            resolved = 0
            print(f"Tickets Resolved: {resolved}")

        if status == "open":
            solve = 0
            solve += 1
            print(f"Tickets To Solve: {solve}")
        else:
            solve = 0
            print(f"Tickets To Solve: {solve}")

        print("")
        print("")

        continue
