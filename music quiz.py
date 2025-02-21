#imports
import time
import random

#subprograms
def login(file_name, username,password):
    file =open (file_name,"r")
    namelist = []
    for line in file:
        namelist.append(line.strip())
    for i in range (0,len(namelist),1):
        if namelist[i] == username and namelist[i+1] == password:
            return ("Username and password correct")
    return ("Not in file")
            
    file.close

#main program
#gets username and password
username = str(input("Enter your username: "))
password = str(input("Enter your password: "))
#
print(login("users.txt", username,password))


