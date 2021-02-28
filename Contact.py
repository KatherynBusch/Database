import mysql.connector
#connect to mySQL database
db = mysql.connector.connect(host='database-1.clx1a3xotfba.us-east-1.rds.amazonaws.com', user='admin',
                             password='kBB918!321')
cursor = db.cursor()

#use the created schema and commit execution
cursor.execute("use newSchema;")
db.commit()
class Contact(): #this class runs the entire program and contains all necessary functions


    def __init__(self):
        print("===Contact Database===")


    def printMenu(self): #prints out starter menu
        print("MENU")
        print("a - Add contact")
        print("d - Remove contact")
        print("u - Update contact details")
        print("b - Output all contacts in alphabetical order")
        print("c - Output all contacts by creation date")
        print("o - Output all contacts")
        print("q - Quit")
        print("Choose an option: ")