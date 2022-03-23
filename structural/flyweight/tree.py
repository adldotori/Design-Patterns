from typing import List


class TreeType(object):
    def __init__(self, name: str, color: str, texture: str):
        self.__name = name
        self.__color = color
        self.__texture = texture

    @property
    def name(self) -> str:
        return self.__name

    @property
    def color(self) -> str:
        return self.__color

    @property
    def texture(self) -> str:
        return self.__texture

    def draw(self, canvas, x, y):
        print(self.__name, x, y)


class Tree(object):
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self, canvas):
        self.tree_type.draw(canvas, self.x, self.y)


class TreeFactory(object):
    tree_types: List[TreeType] = []

    @staticmethod
    def get_tree_type(name, color, texture):
        for tree_type in TreeFactory.tree_types:
            if (
                tree_type.name == name
                and tree_type.color == color
                and tree_type.texture == texture
            ):
                print(f"caching tree type: {name}, {color}, {texture}")
                return tree_type

        tree_type = TreeType(name, color, texture)
        TreeFactory.tree_types.append(tree_type)
        return tree_type


class Forest(object):
    def __init__(self):
        self.trees: List[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str) -> Tree:
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        if tree_type is None:
            return None
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)
        return tree

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)
