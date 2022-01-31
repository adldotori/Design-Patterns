class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_)
        return class_._instance


class MyClass(Singleton):
    def __init__(self, name: str):
        self.name = name


if __name__ == "__main__":
    m1 = MyClass("m1")
    m2 = MyClass("m2")
    print(m1.name, m2.name)
    print(id(m1), id(m2))
