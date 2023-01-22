## Importing Tas sqlhe Libs ##
# Global Libs #
import time
# Local Libs #
from Info import Info

# Instance Info Module #
info = Info()


def userPanel():
    try:
        txt =  '############ Menu ###########\n'
        txt += '#**| 1.Add Cars          |**#\n'
        txt += '#**| 2.Delete Cars       |**#\n'
        txt += '#**| 3.Search Cars       |**#\n'
        txt += '*****************************\n'
        txt += '----------Tickets------------\n'
        txt += '#**| 4.Add Tickets       |**#\n'
        txt += '#**| 5.Delete Tickets    |**#\n'
        txt += '#**| 6.Track Tickets     |**#\n'
        txt += '#**| 7.Exit              |**#\n'
        txt += '*****************************\n'
        txt += "Choose From Options Above: "
        
        navig = info.get_info(txt, 'int')
        
        
        if navig == 1:
            import add_car
        
        elif navig == 2:
            import delete_car_user
        
        elif navig == 3:
            import car_search
        
        elif navig == 4:
            import add_tks
        
        elif navig == 5:
            import delete_tk
        
        elif navig == 6:
            import track_tk
        
        elif navig == 7:
            quit()
            
        else:
            print("Please select a valid navigation.")
            time.sleep(3)
            navig = info.get_info(txt, 'int')
        
    except ValueError:
        print('VALUE ERROR!')
    except TypeError:
        print('TYPE ERROR')
    except ImportError:
        print('Missing File Or Bad File')
    
    except Exception:
        print("Exception ERROR !")