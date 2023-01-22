# Import dependencies
import re
from Helpers import valid_email


#
# @desc Input user information and validate
#
# @param text: str -- The text to show the user
# @param datatype: str -- The datatype of user input to validate
#
# @var data: object -- A variable to hold the user input
#
# @return any -- Depending on datatype
#


class Info:
    # Constructor method
    def __init__(self) -> None:
        pass

    def get_info(self, text: str, datatype: str, lst:list=[]):
        # Python trick for do while
        while True:
            # Input the user data
            data = input(text)

            result = ""

            # Check the type
            try:
                if datatype == 'int':
                    result = int(data)
                    break
                
                elif datatype == 'float':
                    result = float(data)
                    break

                elif datatype == 'name':
                    if self.check_name(data):
                        result = str(data)
                        break
                    
                elif datatype == 'username':
                    if self.check_usrname(data):
                        result = str(data)
                        break

                elif datatype == 'str':
                    result = str(data)
                    break

                elif datatype == 'email':
                    if valid_email(data):
                        result = str(data)
                        break
                    else:
                        print("Invalid email.")
                        continue
                
                elif datatype == 'password':
                    if self.valid_pass(data):
                        result = str(data)
                        break

                elif datatype == 'list':
                    result = str(data)

                    if result in lst: 
                        break
                    else:
                        print(f"Please select from {lst}.")
                        continue

                else:
                    if self.check_name(data):
                        result = str(data)
                        break

            # Handle the errors
            except:
                print(f"{result} must be of type {datatype}.")

        # Return the data
        return result

    # Check user name for correct characters
    # only accepts the English alphabetical characters
    def check_name(self, text: str):
        # Check required model name
        if not text:
            print("The name is required!")
            return False

        elif len(text) < 2:
            print("The name must be at least 2 characters!")
            return False

        # Regular expression
        regex = '^[A-Za-z ]+$'

        # Invalid name
        if not re.match(regex, text):
            print("Invalid characters!")
            return False

        # Valid name
        else:
            return True
        
    # USER NAME CHECKER :
    def check_usrname(self, text: str):
        if not text:
            print("The User Name Is Required!")
            return False
        
        elif len(text) <= 4:
            print("The User Name must be at least 4 characters!")
            return False
        
        elif len(text) > 32:
            print('User Name Can Not be Longer Than 32 Characters!')
            return False
        
        # Regular expression
        regex = '^(?![.-])(?!.*[.]{2})[a-zA-Z0-9.-]+(?<![.])$'
        
        # Invalid User name:
        if not re.match(regex, text):
            print("Invalid characters!")
            return False
        # Valid User Name:
        else:
            return True

    # Password CHECKER :        
    def valid_pass(self, text : str):
        if not text:
            print("The Password Is Required!")
            return False
        
        elif len(text) <= 6:
            print("The Password Must Be At Least 6 Characters!")
            return False
        
        elif len(text) > 80:
            print("The password Can Not Be Longer Than 80 Characters!")
            return False
        
        regx = '^[A-Za-z0-9@#$%^&+=]{8,}$'
        
        # Invalid Password
        if not re.match(regx, text):
            print("Invalid Password try again!")
            return False
        # Valid Pass
        else:
            return True