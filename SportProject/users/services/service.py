from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import transaction

class UserQuery():

    @transaction.non_atomic_requests
    def insertUser(login:str, password:str, mail:str): #Create new user 
     
       user = User.objects.create_user(login, mail, password)

       user.save()
       return("Insert successfully")
       
    
    def selectUser(login:str,Password:str): #Select from user
        UserData = authenticate(username = login, password = Password)
        if UserData is not None:
            return "Authentication is successful"
        else: 
            return "User not found"
        pass

    def changePassword(login:str, newPassword:str):
        user = User.objects.get(username = login)
        user.set_password(newPassword)
        user.save()
        return "Password change succesful"
    def test():
            return(User.objects.filter(username = "111", email = "33333333"))
        


        
               
