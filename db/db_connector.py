import mariadb
from db import db_config

class DbConnector():

    def db_connect(self):
        try:
            conn = mariadb.connect(
                user = db_config.user,
                password = db_config.password,
                host = db_config.host,
                port = db_config.port,
                database = db_config.database
            )
            return conn
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            return None
