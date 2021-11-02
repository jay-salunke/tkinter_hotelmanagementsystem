import mysql.connector


class DBConnection():
    db = mysql.connector.connect(
        host="localhost", user="root", password="Maiboli", database="hotelmanagementsystem")
