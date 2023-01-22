# For creating Database tables
from Database import Database

# models For Creating Database Tabels and etc.
class Models(Database):
    def __init__(self) -> None:
        # Inherit the parent
        super().__init__()
        
        #or ==> Database.__init__(self)
        
        # Create required tables
        self.userInfo()
        self.Tickets()
        self.carsInfo()
        
    
    # Create User Info table
    def userInfo(self):
        sql = """
            CREATE TABLE IF NOT EXISTS userinfo (
              id INTEGER NOT NULL PRIMARY KEY,
              full_name VARCHAR(60) NOT NULL,
              age INTEGER NOT NULL,
              phone_number INTEGER NOT NULL UNIQUE, 
              app_id VARCHAR(255) NOT NULL UNIQUE,
              identity_id INTEGER NOT NULL UNIQUE,
              description TEXT NOT NULL,
              adrs TEXT NOT NULL,
              usr_name VARCHAR(255) NOT NULL UNIQUE,
              email VARCHAR(255) NOT NULL,
              password VARCHAR(255) NOT NULL UNIQUE,
              user_type VARCHAR(255) NOT NULL,
              tk_id VARCHAR(255) NOT NULL UNIQUE,
              read_user BOOLEAN DEFAULT False
            );
        """
        return self.query(sql)
    
    # Create tickets Table
    def Tickets(self):
        sql = """
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER NOT NULL PRIMARY KEY,
                email VARCHAR(100) NOT NULL,
                subject VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                user_type VARCHAR(100) NOT NULL,
                tk_id VARCHAR(255) NOT NUll,
                ticket_token TEXT NOT NULL UNIQUE,
                read_ticket BOOLEAN DEFAULT False
            );
        """
        return self.query(sql)
    
    # Create Cars Info Table
    def carsInfo(self):
        sql = """
            CREATE TABLE IF NOT EXISTS carsinfo (
                id INTEGER NOT NULL PRIMARY KEY,
                car_name VARCHAR(255) NOT NULL,
                c_model INTEGER NOT NULL,
                c_health TEXT NOT NULL,
                track_id VARCHAR(255) NOT NULL UNIQUE,
                c_plate VARCHAR(255) NOT NULL,
                price FLOAT NOT NULL DEFAULT 00.0,
                description TEXT NOT NULL,
                adrs TEXT NOT NULL,
                auth VARCHAR(255) NOT NULL,
                read_car BOOLEAN DEFAULT False
            );
        """
        return self.query(sql)
    
    ################################## CARS ################################################
    def create_car(self, car_name, c_model, c_health, track_id, c_plate, price, description, adrs, auth):
        sql = """
            INSERT INTO carsinfo (car_name, c_model, c_health, track_id, c_plate, price, description, adrs, auth)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        data = [car_name, c_model, c_health, track_id, c_plate, price, description, adrs, auth]
        if self.query(sql, data):
            return track_id
    ###############################################
    ## Authur Validation Who Registered The car? ##
    def fetchAuth(self, auth):
        sql = """
            SELECT * FROM carsinfo
            WHERE auth = ?;
        """
        data = [auth]
        if self.query(sql, data).fetchone():
            return self.query(sql, data).fetchone()
        
        else:
            return False
    
    
    ###############################################
    ## For TRACK Id Search And Validation        ##
    def fetchTrackId(self, track_id):
        sql = """
            SELECT * FROM carsinfo
            WHERE track_id = ?;
        """
        data = [track_id]
        if self.query(sql, data).fetchone():
            return self.query(sql, data).fetchone()
        else:
            return False
    #######################################
        
    ## Search Car By Track Id ##
    def fetch_car(self, track_id):
        sql = """
            SELECT * FROM carsinfo
            WHERE track_id = ?;
        """
        data = [track_id]
        
        if self.query(sql, data).fetchone():
            return self.query(sql, data).fetchone()
        
        else:
            return False

    # Car Status for Delete
    def Car_status(self, track_id):
        sql = """
            SELECT * FROM carsinfo 
            WHERE track_id = ?;
        """
        data = [track_id]
        if len(self.query(sql, data).fetchall()) == 1:
            return self.query(sql, data).fetchone()['read_car']

        else:
            return -1
    
    # Delete A Car From Data Base
    def car_delete(self, del_id):
        sql = """
            DELETE FROM carsinfo
            WHERE track_id = ?;
        """
        data = [del_id]

        if self.query(sql, data):
            return True
        else:
            return False
    
    
    ################################## USERS ###############################################
    # Insert new user into database
    def create_user(self, full_name, age, phone_number, app_id, identity_id, description, adrs, usr_name, email, password, user_type, tk_id):
        sql = """
            INSERT INTO userinfo (full_name, age, phone_number, app_id, identity_id, description, adrs, usr_name, email, password, user_type, tk_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        data = [full_name, age, phone_number, app_id, identity_id, description, adrs, usr_name, email, password, user_type, tk_id]
        if self.query(sql, data):
            return app_id
    
    ######################################################
    ## This Functions Are For User Admin/CEO Login Only ##    
    def logInUserNameCheck(self, usr_name):
        sql = """
            SELECT * FROM userinfo
            WHERE usr_name = ?;
        """
        data = [usr_name]
        # Data exists
        if self.query(sql, data).fetchone():
            return self.query(sql, data).fetchone()

        # Data not exists
        else:
            return False
        
    def logInPassCheck(self, password):
        sql = """
            SELECT * FROM userinfo
            WHERE password = ?;
        """
        data = [password]
        if self.query(sql, data).fetchone():
            return self.query(sql, data).fetchone()
        
        else:
            return False
    ####################################################
    
    # Search User By Id
    def fetch_user(self, app_id):
        sql = """
            SELECT * FROM userinfo
            WHERE app_id = ?;
        """
        data = [app_id]
        
       # User exists
        if self.query(sql, data).fetchone():
            return self.query(sql, data).fetchone()

        # User not exists
        else:
            return False


    # User Status for Delete
    def User_status(self, app_id):
        sql = """
            SELECT * FROM userinfo 
            WHERE app_id = ?;
        """
        data = [app_id]
        if len(self.query(sql, data).fetchall()) == 1:
            return self.query(sql, data).fetchone()['read_user']

        else:
            return -1

    # Delete A User From Data Base
    def user_delete(self, app_id):
        sql = """
            DELETE FROM userinfo
            WHERE app_id = ?;
        """
        data = [app_id]

        if self.query(sql, data):
            return True
        else:
            return False

########################################## TICKETS ###########################################################
# Insert new Ticket into database + Shows Contact us info
    def create_ticket(self, email, subject, description, user_type, tk_id, ticket_token):
        sql = """
            INSERT INTO tickets (email, subject, description, user_type, tk_id, ticket_token)
            VALUES (?, ?, ?, ?, ?, ?);
        """
        data = [email, subject, description, user_type, tk_id, ticket_token]

        if self.query(sql, data):
            return ticket_token
        
    ########################################
    ## For Tk Id Search And Validation ##
    def fetch_tkid(self, tk_id):
        sql = """
            SELECT * FROM userinfo
            WHERE tk_id = ?;
        """
        data = [tk_id]
        if self.query(sql, data).fetchone():
            return self.query(sql, data).fetchone()
        else:
            return False
    #######################################
    
    # Tickets Status In Database
    def ticket_status(self, ticket_token):
        sql = """
            SELECT * FROM tickets 
            WHERE ticket_token = ?;
        """
        data = [ticket_token]
        if len(self.query(sql, data).fetchall()) == 1:
            return self.query(sql, data).fetchone()['read_ticket']

        else:
            return -1

    # Process Tickets In Database
    def ticket_process(self, ticket_token):
        sql = """
            UPDATE tickets SET read_ticket = True
            WHERE ticket_token = ?;
        """
        data = [ticket_token]

        if self.query(sql, data):
            return True
        else:
            return False

    # Delete Tickets From Database
    def ticket_delete(self, ticket_token):
        sql = """
            DELETE FROM tickets
            WHERE ticket_token = ?;
        """
        data = [ticket_token]

        if self.query(sql, data):
            return True
        else:
            return False