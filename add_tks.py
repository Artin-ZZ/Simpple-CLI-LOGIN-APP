# Import dependencies
from Info import Info
from Models import Models
from Helpers import random_string


# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Send Ticket.")

# Prompt the user for require info
email = info.get_info('User Email: ', 'email')
user_type = info.get_info("User Type (User Tickets-> [USTK]/Car Tickets-> [CATK]): ", datatype="list", lst=["USTK", "CATK"])
subject = info.get_info("Ticket Subject: ", 'str')
description = info.get_info('Ticket Description: ', 'str')
tk_id = info.get_info("Enter Your Ticket ID: ", 'str')
ticket_token = random_string()

# Create ticket
# ticket_token = db.create_ticket(email, subject, description, user_type, app_id, ticket_token)

if user_type == "USTK":
    if db.fetch_tkid(tk_id=tk_id):
        # Success
        ticket_add = db.create_ticket(email, subject, description, user_type, tk_id,ticket_token)
        message = f"Your Ticket Has Been Submitted Successfully!\n"
        message += f"Your tracking code is: {ticket_token}"
        print(message)
    
elif user_type == 'CATK':
    state_buis = info.get_info("State Your Buisness(Car Buy/Sell--> cbs | Car Problems --> cp): ", 'list', ['cbs', 'cp'])
    
    if state_buis == 'cbs':
        track_id = info.get_info("Your Car Track Id: ", 'str')
        if db.fetchTrackId(track_id=track_id):
            # Success
            ticket_add = db.create_ticket(email, subject, description, user_type, tk_id,ticket_token)
            message = f"Your Ticket Has Been Submitted Successfully!\n"
            message += f"Your tracking code is: {ticket_token}"
            print(message)
    
    else:
        ticket_add = db.create_ticket(email, subject, description, user_type, tk_id,ticket_token)
        message = f"Your Ticket Has Been Submitted Successfully!\n"
        message += f"Your tracking code is: {ticket_token}"
        print(message)

else:
    # Fail
    print("Car/Ticket Id Is Invalid Please Register a user & car First!")