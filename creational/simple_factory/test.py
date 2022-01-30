from main import UserFactory
import pytest


class Test(object):
    def test_admin(self):
        user = UserFactory.create_user("admin")
        print("[+] type:", user.get_type())
        user.action()

    def test_normal(self):
        user = UserFactory.create_user("normal")
        print("[+] type:", user.get_type())
        user.action()

    def test_other(self):
        with pytest.raises(KeyError):
            user = UserFactory.create_user("other")
            print("[+] type:", user.get_type())
            user.action()
