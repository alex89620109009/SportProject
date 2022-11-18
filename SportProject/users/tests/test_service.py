from django.test import TestCase
from users.services.service import UserQuery
from users.services.service import insertUser
# from django.contrib.auth.models import User

class ServicesestClass(TestCase):
    # TestCase создает чистую базу данных перед запуском своих методов,
    #А также запускает каждую функцию тестирования в его собственной транзакции

    @classmethod
    def setUpTestData(self):
        # Вызывается каждый раз перед запуском теста на уровне настройки всего класса
        #Данный метод нужен для создания объекто, которые не буду модифицироваться/изменяться в каком-либо из тестовых методов
        mail = ""
        pass

    def SetUp(self):
        #Вызывается перед каждой тестовой функции для настройки объектов
        #Которые могут изменяться во время тестов
        pass

    
    
