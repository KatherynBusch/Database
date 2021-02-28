from Contact import *
from datetime import date
#call a Contact class
cont = Contact()
#run program forever until quit is called
while True:
   cont.printMenu()
   ans = str(input())
   #run necessary function based on user input and get necessary parameters
   # call error if given invalid input
   if ans == 'q':
       break;
   elif ans == 'a':
       name = str(input("Enter the Contact Name: "))
       cDate = str(input("Enter the creation date in YYYY-MM-DD format, or type 1 to use today: "))
       if cDate == '1':
           cDate = date.today()
       #call class function
       cont.addContact(name,cDate)
   elif ans == 'd':
       id = str(input("Enter the Contact ID to delete (if found): "))
       # call class function
       cont.removeContact(id)

   elif ans == 'u':
       id = str(input("Enter the Contact ID to update (if found): "))
       col = str(input("Enter the column you would like to update (if found): "))
       val = str(input("Enter the new value you would like to update: "))
       # call class function
       cont.updateContact(id,col,val)
   elif ans == 'b':
       # call class function
       cont.outputContactsAlphabetically()
   elif ans == 'c':
       # call class function
       cont.outputContactsByDate()
   elif ans == 'o':
       # call class function
       cont.outputAll()
   else:
       print("Error, invalid input. Please try again.")
   print("")

