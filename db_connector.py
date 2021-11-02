from dotenv import load_dotenv
import os
import mysql.connector


class DBConnection():
    

    def __init__(self):
        load_dotenv()
        self.db = mysql.connector.connect(
        host="localhost", user="root", password=os.getenv("DB_PASSWORD"), database="hotelmanagementsystem")