from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def action(self):
        raise NotImplementedError()


class AdminUser(User):
    def __init__(self):
        self.__type = "admin"

    def get_type(self) -> str:
        return self.__type

    def action(self):
        print("[+] admin user action")

    def __str__(self) -> str:
        return "admin user"


class NormalUser(User):
    def __init__(self):
        self.__type = "normal"

    def get_type(self) -> str:
        return self.__type

    def action(self):
        print("[+] normal user action")

    def __str__(self) -> str:
        return "normal user"


class UserFactory(object):
    @staticmethod
    def create_user(user_type: str) -> User:
        if user_type == "admin":
            return AdminUser()
        elif user_type == "normal":
            return NormalUser()
        else:
            raise KeyError("unknown user type")


if __name__ == "__main__":
    user = UserFactory.create_user("admin")
    print("[+] type:", user.get_type())
    user.action()
