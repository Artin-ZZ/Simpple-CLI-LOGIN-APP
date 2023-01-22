## Importing Tas sqlhe Libs ##
# Global Libs #
import os, time
# Local Libs #
from Info import Info

# Instance Info Module #
info = Info()


def adminPanel():
    try:
        txt =  '############ Menu ###########\n'
        txt += '-----------Users-------------\n'
        txt += '#**| 1.Greet             |**#\n'
        txt += '#**| 2.Add User          |**#\n'
        txt += '#**| 3.Delete User       |**#\n'
        txt += '#**| 4.Search Users      |**#\n'
        txt += '*****************************\n'
        txt += '----------Tickets------------\n'
        txt += '#**| 5.Add Tickets       |**#\n'
        txt += '#**| 6.Delete Tickets    |**#\n'
        txt += '#**| 7.Track Tickets     |**#\n'
        txt += '#**| 8.Process Tickets   |**#\n'
        txt += '*****************************\n'
        txt += '-----------Cars--------------\n'
        txt += '#**| 9.Add Cars          |**#\n'
        txt += '#**| 10.Delete Cars      |**#\n'
        txt += '#**| 11.Search Cars      |**#\n'
        txt += '#**| 12.Exit             |**#\n'
        txt += '*****************************\n'
        txt += "Choose From Options Above: "
        nav = info.get_info(txt, 'int')
        
        
        if nav == 1:
            def greetUser(name):
                os.system('cls')
                print(f"Hello Dear {name} Welcome :)")
            greetUser(info.get_info("Enter Name: ", 'str'))
            
        
        elif nav == 2:
            import add_user
            
        elif nav == 3:
            import delete_user
        
        elif nav == 4:
            import user_search
        
        elif nav == 5:
            import add_tks
            
        elif nav == 6:
            import delete_tk
        
        elif nav == 7:
            import track_tk
        
        elif nav == 8:
            import process_tk
                        
        elif nav == 9:
            import add_car
        
        elif nav == 10:
            import delete_car
        
        elif nav == 11:
            import car_search
        
        elif nav == 12:
            quit()
        
        else:
            print("Please select a valid navigation.")
            time.sleep(3)
            nav = info.get_info(txt, 'int')
            
        
    except ValueError:
        print('VALUE ERROR!')
    except TypeError:
        print('TYPE ERROR')
    except ImportError:
        print('Missing File Or Bad File')
    except Exception:
        print("Exception ERROR !")