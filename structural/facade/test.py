import pytest
from video import VideoConverter


def test():
    converter = VideoConverter()
    print(converter.convert("test.mp4", "mp4"))
    print(converter.convert("test.ogg", "ogg"))
