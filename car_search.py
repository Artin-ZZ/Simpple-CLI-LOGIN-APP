# Dependencies
import os
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# For Test
# user_grades = db.query("SELECT * FROM grades WHERE student_id = 1 ORDER BY id DESC").fetchone()
# print(user_grades)

# Page title
print("--------Search Car by Track ID----------")

# Prompt for the Car Track ID
track_id = info.get_info('Car Track ID: ', 'str')
os.system('cls')


# Check for existense
if not db.fetch_car(track_id):
    print("Car doesn't exist!")
    exit()

# Print the Car info
car = db.fetch_car(track_id)

result =  "------------------------- CAR FOUND -------------------------\n"
result += f"""|Car Name: {car['car_name']} \n|Car Model: {car['c_model']} \n|Car Health: {car['c_health']}  \n|Track ID: {car['track_id']}  \n|Car Plate No: {car['c_plate']} \n|Price: {car['price']} \n|Description: {car['description']} \n|Address: {car['adrs']}\n"""
result += "-------------------------------------------------------------\n"

print(result)