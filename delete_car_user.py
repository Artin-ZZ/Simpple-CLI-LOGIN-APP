# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Delete A Car.")

# Prompt for the app id
track_id = info.get_info('Car Track ID: ', 'str')
auth = info.get_info("Type in Your User Name: ", 'username')



# car status
car_status = db.Car_status(track_id)

if not car_status == -1:
    if db.fetchAuth(auth=auth):
        # Prompt admin to confirm the process
        confirm = info.get_info('Do you want to delete this Car? (y/n) ', 'list', ['y', 'n'])

        if confirm == 'y':
            # Delete from database
            if db.car_delete(track_id):
                message = "The Car Was deleted successfully!"
            else:
                message = "Oops, an error occoured!"

        # Rejected
        else:
            message = "The process has been cancelled!"
    else:
        message = "Wrong User Name Or Does Not Exist!"

else:
    message = "The Car doesn't exist!"

# print result
print(message)


# if not db.Car_status(track_id) == -1:
#     if db.fetchAuth(auth=auth):
#         confirm = info.get_info('Do you want to delete this Car? (y/n) ', 'list', ['y', 'n'])
        
#         if confirm == 'y':
#             # Delete from database
#             if db.car_delete(track_id) and db.fetchAuth(auth=auth):
#                 message = "The Car Was deleted successfully!"
#             else:
#                 message = "Oops, an error occoured Or Wrong user Name!"
        
#         # Rejected
#         else:
#             message = "The process has been cancelled!"
            
# else:
#     message = "The Car doesn't exist Or Wrong user Name/Track ID!"
    
# # print result
# print(message)