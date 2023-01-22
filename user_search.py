# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# For Test
# user_grades = db.query("SELECT * FROM grades WHERE student_id = 1 ORDER BY id DESC").fetchone()
# print(user_grades)

# Page title
print("--------Search User by ID----------")

# Prompt for the student id
app_id = info.get_info('app Id: ', 'int')


# Check for existense
if not db.fetch_user(app_id):
    print("User doesn't exist!")
    exit()

# Print the student info
user = db.fetch_user(app_id)

result = f"""|Name: {user['full_name']} \n|Age: {user['age']} \n|Phone: {user['phone_number']}  \n|App ID: {user['app_id']}  \n|Identity ID: {user['identity_id']} \n|Description: {user['description']} \n|Address: {user['adrs']} \n|User Name: {user['usr_name']} \n|Email: {user['email']} \n|Password: {user['password']}\n"""



print(result)