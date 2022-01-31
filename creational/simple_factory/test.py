from main import UserFactory
import pytest


TYPE_CONST = "[+] type:"


class Test(object):
    def test_admin(self):
        user = UserFactory.create_user("admin")
        print(TYPE_CONST, user.get_type())
        user.action()

    def test_normal(self):
        user = UserFactory.create_user("normal")
        print(TYPE_CONST, user.get_type())
        user.action()

    def test_other(self):
        with pytest.raises(KeyError):
            user = UserFactory.create_user("other")
            print(TYPE_CONST, user.get_type())
            user.action()
