from graphic import CompoundGraphic, Dot, Circle


class ImageEditor(object):
    def __init__(self):
        self.all = CompoundGraphic()

    def add_dot(self, x, y):
        dot = Dot(x, y)
        self.all.add(dot)
        return dot

    def add_circle(self, x, y, r):
        circle = Circle(x, y, r)
        self.all.add(circle)
        return circle

    def group_selected(self, *graphics):
        self.graphic = CompoundGraphic()
        for graphic in graphics:
            self.graphic.add(graphic)
            self.all.remove(graphic)
        self.all.add(self.graphic)
        return self.graphic

    def move(self, x, y, *graphics):
        for graphic in graphics:
            graphic.move(x, y)

    def draw(self):
        return self.all.draw()


if __name__ == "__main__":
    editor = ImageEditor()
    dot1 = editor.add_dot(10, 10)
    dot2 = editor.add_dot(5, 2)
    circle = editor.add_circle(20, 20, 10)
    print(editor.draw())

    editor.move(0, 0, dot1)
    print(editor.draw())

    group = editor.group_selected(dot1, circle)
    editor.move(-5, -5, group)
    print(editor.draw())
