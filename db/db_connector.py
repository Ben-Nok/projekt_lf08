import mariadb
from db.db_config import get_db_config

class DbConnector():

    def __init__(self) -> None:
        self.config = get_db_config()
        pass

    def db_connect(self):
        #db connection as class instance
        try:
            #create and return connection
            return mariadb.connect(**self.config)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            return None
