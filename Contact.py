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

   def addContact(self,name,date):
       #add given parameters to an SQL query
       string = "INSERT INTO contacts (contactDetails,creationDate) values (" +'\''+ name +'\''+", "+'\''+ str(date)+'\'' + ");"
       #execute and commit query
       cursor.execute(string)
       db.commit()
       return ""

   def removeContact(self,id):
       # add given parameters to an SQL query
       string = "DELETE FROM contacts WHERE id = " + str(id) + ";"
       # execute and commit query
       cursor.execute(string)
       db.commit()


   def updateContact(self,id, column, value):
       # add given parameters to an SQL query
       string = "UPDATE contacts SET " + column + " = "+'\''+ str(value) +'\''+ " WHERE id = " + str(id) + ";"

       # execute and commit query
       cursor.execute(string)
       db.commit()
       return ""

   def outputContactsAlphabetically(self):
       #call SQL query, ordering by contactDetails
       cursor.execute("SELECT * FROM contacts ORDER BY contactDetails ASC;")
       #add result to a list and loop through each item to print it out
       rows = cursor.fetchall()
       print("ID    Contact Details    Date")
       for row in rows:
           print("[" + str(row[0]) + "]" + " , " + row[1] + " , " + str(row[2]))


   def outputContactsByDate(self):
       # call SQL query, ordering by creationDate
       cursor.execute("SELECT * FROM contacts ORDER BY creationDate DESC;")
       # add result to a list and loop through each item to print it out
       rows = cursor.fetchall()
       print("ID    Contact Details    Date")
       for row in rows:
           print("[" + str(row[0]) + "]" + " , " + row[1] + " , " + str(row[2]))


   def outputAll(self):
           cursor.execute("SELECT * FROM contacts;")
           # add result to a list and loop through each item to print it out
           rows = cursor.fetchall()
           print("ID    Contact     Date")
           for row in rows:
               print("[" + str(row[0]) + "]" + " , " + row[1] + " , " + str(row[2]))


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
