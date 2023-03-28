import mysql.connector
import sys
from user import *
from mysql.connector import Error

class Seller(User):
    def __init__(self,userid,firstname,lastname,password,telephone,email,userType):
        super().__init__(userid,firstname,lastname,password,telephone,email,userType)


    def addInv(self, cursor, connection):
         #initialize cursor and connection
            cursor = cursor
            connection = connection
            #get user input for isbn
            isbn = input("ISBN: ")
            #verify isbn does not already exist
            check_query = ("SELECT ISBN FROM inventory WHERE ISBN = %s")
            cursor.execute(check_query, (isbn,))
            inv = cursor.fetchall()
            #if it does not, continue taking input
            if(inv == []):
                title = input("Title: ")
                author = input("Author: ")
                stock = input("Stock: ")
                genre = input("Genre: ")
                pubYear = int(input("Publishing Year: "))
                publisher = input("Publisher: ")
                susFlag = 1
                price = float(input("Price: "))
                seller = self.userid
                #insert information into new row in inventory
                in_query = ("INSERT INTO inventory VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                data = (isbn, title, author, stock, genre, pubYear, publisher, susFlag, price, seller)
                cursor.execute(in_query,data)
                connection.commit()
            #if isbn does already exist, error
            else:
                print("That ISBN already exists in the database :(")
            cursor.close()
            connection.close()

    def remInv(self, cursor, connection):
        item = input("ISBN of product to Remove: ")
        print("Please input password below to verify deleting this entry: ")
        check = self.checkPassword(cursor)
        if(check == True):
            query = "DELETE FROM cart WHERE ISBN=%s"
            data = (item,)
            cursor.execute(query, data)
            connection.commit()
            print(cursor.rowcount, "record deleted.")
        else:
            print("Could not delete item")
        cursor.close()
        connection.close()

