from main import MyClass


class Test(object):
    def test(self):
        m1 = MyClass("m1")
        m2 = MyClass("m2")
        print(m1.name, m2.name)
        print(id(m1), id(m2))

        assert id(m1) == id(m2)
