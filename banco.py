import sqlite3
from datetime import datetime


class BancoDados():
    def __init__(self) -> None:
        self.con = sqlite3.connect("pydb.db")
        self.create_table()

    def create_table(self):
        cursor = self.con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id_users INTEGER PRIMARY KEY, email TEXT, passwrd TEXT, UNIQUE(email) )")
        self.con.commit()
        cursor.execute("CREATE TABLE IF NOT EXISTS last_login (id_last_login INTEGER PRIMARY KEY, id_users INTEGER, last_login TEXT,remember INTEGER, FOREIGN KEY (id_users) REFERENCES users(id_users) )")
        self.con.commit()
            
    def insert_table_users(self,values:list):
        cursor = self.con.cursor()
        cursor.execute(f"INSERT INTO users VALUES (NULL,'{values[0]}','{values[1]}')")
        self.con.commit()
        cursor.close()

    def select_table_users(self):
        cursor = self.con.cursor()
        resultado = cursor.execute('SELECT * FROM users')
        cursor.close()
        return resultado
    
    def select_email_password_users(self,email:str,password:str):
        cursor = self.con.cursor()
        resultado = cursor.execute(f"SELECT * FROM users WHERE email = '{email}' and passwrd = '{password}'")
        return resultado.fetchone()
    
    def insert_table_last_login(self,id_users:int,remember:int):
        cursor = self.con.cursor()
        cursor.execute(f"INSERT INTO last_login VALUES (NULL,{id_users},'{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}',{1 if remember else 0})")
        self.con.commit()
        cursor.close()
    
    def select_table_last_login(self,id_users:int):
        cursor = self.con.cursor()
        resultado = cursor.execute(f"SELECT remember FROM last_login WHERE id_users={id_users}")
        cursor.close()
        return resultado.lastrowid
