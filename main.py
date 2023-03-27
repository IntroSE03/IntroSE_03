import mysql.connector
import sys
from mysql.connector import Error
from seller import *

def Connect_db():
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="introse_03")
        print("Successful connection.")
        cursor = connection.cursor()
        return connection, cursor
    except Error as e:
        print("error connecting to the database: ", e)
        sys.exit()
    except:
        print("Failed connection.")
        sys.exit()

def Curr_user(cursor):
    u = login(cursor)
    return Seller(u.userid,u.firstname,u.lastname,u.password,u.telephone,u.email,u.userType)


def main():
    connection, cursor = Connect_db()
    curr_user = Curr_user(cursor)
    curr_user.addInv(cursor,connection)

main()

