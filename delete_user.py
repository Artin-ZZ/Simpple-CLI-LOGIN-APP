# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Delete A User.")

# Prompt for the app id
app_id = info.get_info('User Id: ', 'int')

# User status
usr_status = db.User_status(app_id)

if not usr_status == -1:
    # Prompt admin to confirm the process
    confirm = info.get_info('Do you want to delete this User? (y/n) ', 'list', ['y', 'n'])

    if confirm == 'y':
        # Delete from database
        if db.user_delete(app_id):
            message = "The User Was deleted successfully!"
        else:
            message = "Oops, an error occoured!!"

    # Rejected
    else:
        message = "The process has been cancelled!"

else:
    message = "The User doesn't exist!"

# print result
print(message)
