from django.test import TestCase
from users.services.service import UserQuery
from django.contrib.auth.models import User

class ServicesTestClass(TestCase):
    # TestCase создает чистую базу данных перед запуском своих методов,
    #А также запускает каждую функцию тестирования в его собственной транзакции
    """ Класс для теста функций из services.py"""


    @classmethod
    def setUpTestData(cls):
        # Вызывается каждый раз перед запуском теста на уровне настройки всего класса
        #Данный метод нужен для создания объектов, которые не буду модифицироваться/изменяться в каком-либо из тестовых методов
        pass

    def setUp(self):
        #Вызывается перед каждой тестовой функции для настройки объектов
        #Которые могут изменяться во время тестов
        for i in range(1,6):
            User.objects.create_user("Bob"+str(i),"example"+str(i)+"@mail.ru","good_password"+str(i))
        
    def test_insert_user(self):
        """Тест по созданию пользователя"""
        TestUser = UserQuery.insertUser(login="Bob123",password="123",mail="")
        SecondUser = UserQuery.insertUser(login="Bob31",password="1234567", mail="examplag@mail.ru")
        self.assertEqual("The password doesn't fit", TestUser) #Проверка на совпадение левого аргумента и правого
        self.assertEqual("Insert successfully", SecondUser)

    def test_select_user(self):
        """Аутентификация пользователя"""
        first = UserQuery.selectUser(login="Bob1",Password="good_password1")
        second = UserQuery.selectUser(login="Bob2",Password="good_password2")
        third = UserQuery.selectUser(login="123", Password="123")

        self.assertEqual("Authentication is successful", first)
        self.assertEqual("Authentication is successful", second)
        self.assertEqual("User not found", third)

    def test_change_password(self):
        """Смена пароля"""
        """При тесте UserThird прога выпадает с ошибкой, поскольку пользователя с таким логином не существует
            Возможно стоит добавить проверку на то, что принимаемый пароль идентичен изменяемому, т.е совпадает старый пароль с новым        
        """
        FirstUser = UserQuery.changePassword(login="Bob1",newPassword="123")
        SecondUser = UserQuery.changePassword(login="Bob2", newPassword="good_password2")
        ThirdUser = UserQuery.changePassword(login="12312312", newPassword="dgfdfgdf")

        self.assertEqual("The password doesn't fit",FirstUser)
        self.assertEqual("Password change succesful",SecondUser)
        self.assertEqual("The password doesn't fit",ThirdUser)
        pass
        


    
    
    
