from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import transaction
import os

class UserQuery():
    __checkPassword = lambda password: len(password) >= 6

        
    @transaction.non_atomic_requests
    def insertUser(login:str, password:str, mail:str): #Create new user 
     if UserQuery.__checkPassword(password):
       user = User.objects.create_user(login, mail, password)
       user.save()
       return("Insert successfully")
     else:
         return("The password doesn't fit")
    
       
    
    def selectUser(login:str,Password:str): #Select from user
        UserData = authenticate(username = login, password = Password)
        if UserData is not None:
            
            return "Authentication is successful"
        else: 
            return "User not found"
        pass

    def changePassword(login:str, newPassword:str):
        user = User.objects.get(username = login)
        if UserQuery.__checkPassword(newPassword):
            user.set_password(newPassword)
            user.save()
            return "Password change succesful"
        else:
            return("The password doesn't fit")

    @transaction.non_atomic_requests
    def changeInfo(login:str, **info):
        user = User.objects.get(username = login)
        for key, value in info.items():
            match key:
                case "first_name":
                    user.first_name = value
                    print(f"Field '{key}' can be changed")
                case "last_name":
                    user.last_name = value
                    print(f"Field '{key}' can be changed")
                case "email":
                    user.email = value
                    print(f"Field '{key}' can be changed")
                case _:
                    print(f"Field '{key}' not understood, transaction canceled")
        user.save()
       
    def makeUserFolder(username):
        try:
            os.makedirs(f"UserFolders/{username}/img")
            return "Folder maked."
        except Exception as ex: 
            return f"The folder {username} exists.\n {ex}"
        


        
               
