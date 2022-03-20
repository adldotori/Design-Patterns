import pytest

from main import ImageEditor


@pytest.fixture
def editor():
    editor = ImageEditor()
    dot1 = editor.add_dot(10, 10)
    dot2 = editor.add_dot(5, 2)
    circle = editor.add_circle(20, 20, 10)
    return editor, dot1, dot2, circle


def test_draw(editor):
    editor, dot1, dot2, circle = editor
    ans = editor.draw()

    assert ans == "10, 10: .\n5, 2: .\n20, 20: o"


def test_move(editor):
    editor, dot1, dot2, circle = editor
    editor.move(0, 0, dot1)
    ans = editor.draw()

    assert ans == "0, 0: .\n5, 2: .\n20, 20: o"


def test_group(editor):
    editor, dot1, dot2, circle = editor
    editor.move(0, 0, dot1)
    group = editor.group_selected(dot1, circle)
    editor.move(-5, -5, group)
    ans = editor.draw()

    assert ans == "5, 2: .\n-5, -5: .\n-5, -5: o"
