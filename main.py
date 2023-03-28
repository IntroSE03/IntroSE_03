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

def Select_user(cursor):
    u = login(cursor)
    query = ("SELECT usertype FROM people WHERE userid = %s")
    cursor.execute(query, (u.userid,))
    res = cursor.fetchall()
    if(res == "S"):
        return Seller(u.userid,u.firstname,u.lastname,u.password,u.telephone,u.email,u.userType)
    elif(res == "C"):
        print("This is for a customer user, functionality has not been added yet")
    elif(res == "A"):
        print("This is for an admin user, functionality has not been added yet")

def main():
    connection, cursor = Connect_db()
    curr_user = Select_user(cursor)

    curr_user.addInv(cursor,connection)

main()

