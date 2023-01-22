# Import dependencies
from Info import Info
from Models import Models
from Helpers import randomTrackId


# Instatntiate the required classes
db = Models()
info = Info()


# Page title
print("Type In Your Info In Order To Register A Car.")


# App Text Boxes
car_name = info.get_info("Car Full Name: ", 'str')
c_model = info.get_info("Car Model (Year): ", 'str')
c_health = info.get_info("Car Health: ", 'str')
track_id = randomTrackId()
c_plate = info.get_info("Car Plate Number: ", 'str')
price = info.get_info("Car price/Worth: ", 'float')
description = info.get_info("car Description: ", 'str')
adrs = info.get_info("Car Address(Where Is The Car Right Now?): ", 'str')
auth = info.get_info("Type In Your User Name: ", 'username')



if db.logInUserNameCheck(usr_name=auth):
    add_car = db.create_car(car_name, c_model, c_health, track_id, c_plate, price, description, adrs, auth)
    print('Car Was Registered.')

else:
    print('Invalid User name Try Again!')

# # Add To Data Base #
# add_car = db.create_car(car_name, c_model, c_health, track_id, c_plate, price, description, adrs, auth)
# print('Car Was Registered.')