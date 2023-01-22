# Import dependencies
from Info import Info
from Models import Models
from Helpers import random_id, random_tkid

# Instatntiate the required classes
db = Models()
info = Info()


# Page title
print("Enter Info In Order To Register Users.")

# App Text Boxes
full_name = info.get_info("Your Full Name Here: ", 'name')
age = info.get_info('Your Age: ', 'int')
phone_number = info.get_info("Your Phone Number: ", 'int')
app_id = random_id()
identity_id = info.get_info("Your Identity ID: ", 'int')
description = info.get_info("Describtion: ", 'str')
adrs = info.get_info("Your Home/Work Address: ", 'str')

print("""username is 4-32 characters long\n
no _,- or . at the beginning\n
no __ or . or . or .. or .- or _- inside\n
no _,- or . at the end\n""")

usr_name = info.get_info("Choose a User Name: ", 'username')
email = info.get_info("Type In Your Email: ", 'email')
password = info.get_info("Type In Your Password(Choose Carefully): ", 'password')
user_type = info.get_info("User Type Select From The List You See [Admin , CEO , User, Guest]: ", 'list', ['Admin', 'CEO', 'User', 'Guest'])
tk_id = random_tkid()

# Insert The Infos Into Our Database
db.create_user(full_name, age, phone_number, app_id, identity_id, description, adrs, usr_name, email, password, user_type, tk_id)

# Success Message
print('The User Was Created Succesfully')