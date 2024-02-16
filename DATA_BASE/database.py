import sqlite3

from config import db_name


class database_user:
    def __init__(self,DB_NAME):
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()
    def add_new_user(self,tg_id,l_name,f_name):
        self.cursor.execute(f"INSERT INTO users (first_name,last_name,tg_id)"
                            f"VALUES (?,?,?);",(f_name,l_name,tg_id))
        self.connection.commit()
    def update_user(self,tg_id,phone):
        self.cursor.execute(f"UPDATE users SET phone=?"
                            f"Where tg_id=?;",(phone,tg_id))
        self.connection.commit()
    def get_user(self,tg_id):
        user = self.cursor.execute(f"SELECT * FROM users WHERE tg_id={tg_id};")
        return user.fetchone()
    def update_admin(self,tg_id,new_admin_id):
        self.cursor.execute(f"UPDATE users SET admin_id=?"
                            f"Where tg_id=?;",(new_admin_id,tg_id))
        self.connection.commit()
    def __dell__(self):
        self.cursor.close()
        self.connection.close()
class database_movie:
    def __init__(self,DB_NAME):
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()
    def add_new_movie(self,file_id,key,des = None):
        self.cursor.execute(f"INSERT INTO movies (file_id,about,key)"
                            f"VALUES (?,?,?);",(file_id,des,key))
        self.connection.commit()
    def get_movie(self,key):
        user = self.cursor.execute(f"SELECT * FROM movies WHERE key={key};")
        return user.fetchone()
    def __dell__(self):
        self.cursor.close()
        self.connection.close()
