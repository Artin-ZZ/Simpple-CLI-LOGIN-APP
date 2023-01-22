## Importing Libs ##
from Info import Info
from Models import Models

# Instance Info Module #
info = Info()
db = Models()



class LogIn:
    def __init__(self) -> None:
        
        # App Title
        print("---------------- LOG IN PAGE----------------")
        
        # App Text Boxes #
        user_type = info.get_info("Select User Type (CEO,Admin,User,Guest): ", 'list', ['CEO', 'Admin', 'User', 'Guest'])
        
        
        
        
        if user_type == 'CEO':
            user_name = info.get_info("Enter Your User Name: ", 'username')
            password = info.get_info("Your Password: ", 'password')
            
            if db.logInUserNameCheck(user_name) and db.logInPassCheck(password):
                print('Log IN Was Successfull.')
                from Admin_pnl import adminPanel
                run = adminPanel()
                
            else:
                print("Wrong Password/User Name Or User Does Not Exist!")
        
        elif user_type == 'Admin':
            user_name = info.get_info("Enter Your User Name: ", 'username')
            password = info.get_info("Your Password: ", 'password')
            
            if db.logInUserNameCheck(user_name) and db.logInPassCheck(password):
                print('Log IN Was Successfull.')
                from Admin_pnl import adminPanel
                rn = adminPanel()
                   
            else:
                print("Wrong Password/User Name Or User Does Not Exist!")
        
        elif user_type == 'User':
            user_name = info.get_info("Enter Your User Name: ", 'username')
            password = info.get_info("Your Password: ", 'password')
            
            if db.logInUserNameCheck(user_name) and db.logInPassCheck(password):
                print('Log IN Was Successfull.')
                from User_pnl import userPanel
                rns = userPanel()
            
            else:
                print("Wrong Password/User Name Or User Does Not Exist!")
        
        elif user_type == 'Guest':
            print("This Login Panel Is Not For Normal Users CEO & Admins & Users Only!")

if __name__ == "__main__":
    LogIn()