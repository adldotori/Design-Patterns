from prototype import Prototype, ConcretePrototype, SubClassPrototype


class Test(object):
    def test_concrete(self):
        p1 = ConcretePrototype("p1")
        p2 = p1.clone()
        print("p1:", p1)
        print("p2:", p2)
        print("Is it same?", p1 == p2, "\n")

    def tet_subclass(self):
        p3 = SubClassPrototype("p3", 3)
        p4 = p3.clone()
        print("p3:", p3)
        print("p4:", p4)
        print("Is it same?", p3 == p4, "\n")
