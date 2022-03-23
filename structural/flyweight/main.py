from tree import Forest

if __name__ == "__main__":
    forest = Forest()
    forest.plant_tree(0, 0, "oak", "green", "smooth")
    forest.plant_tree(1, 1, "oak", "green", "smooth")
    forest.plant_tree(2, 2, "oak", "green", "smooth")

    canvas = "canvas"
    forest.draw(canvas)
