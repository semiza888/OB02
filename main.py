# Cистема управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.

class User:
    def __init__(self, user_id, name, age):
        self.__private_user_id = user_id     # приватный атрибут
        self.public_name = name              # публичный атрибут
        self._protected_age = age            # защищенный атрибут

    def get_private_user_id(self):           # получение информации get из приватного атрибута
        return self.__private_user_id

    def get_protected_age(self):             # получение информации get из защищенного атрибута
        return self._protected_age

class Admin(User):
    def __init__(self, user_id, name, age):
        super().__init__(user_id, name, age)
        self.__private_access_level = 'admin'  # приватный атрибут

    def set_private_access_level(self):        # установка нового значения set из приватного атрибута
        return self.__private_access_level

    # Добавление нового сотрудника в список users.
    def add_user(self, users, user):
        if not any(u.get_private_user_id() == user.get_private_user_id() for u in users):
            users.append(user)
            print(f"Сотрудник {user.public_name} успешно добавлен.")
        else:
            print(f"Сотрудник с ID {user.get_private_user_id()} уже существует.")

    # Сотрудник удаляется по ID из списка users.
    def remove_user(self, users, user_id):
        for i, user in enumerate(users):
            if user.get_private_user_id() == user_id:
                del users[i]
                print(f"Сотрудник {user.public_name} успешно удален.")
                return
        print(f"Сотрудник с ID {user_id} не найден.")

# Создание списка сотрудников и добавление новых сотрудников
users_list = []
admin = Admin(user_id=1, name="Сергей Петров", age=42)

# Создаем список несколько обычных сотрудников
user1 = User(user_id=2, name="Елена Смирнова", age=35)
user2 = User(user_id=3, name="Николай Иванов", age=28)

# Админ добавляет сотрудников
admin.add_user(users_list, user1)
admin.add_user(users_list, user2)

# Попытка добавить сотрудника с уже существующим ID
admin.add_user(users_list, User(user_id=2, name="Сотрудник уже существует", age=30))

# Удаление сотрудника из списка
admin.remove_user(users_list, 2)

# Попытка удалить несуществующего сотрудника
admin.remove_user(users_list, 99)

