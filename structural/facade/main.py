from video import VideoConverter

if __name__ == "__main__":
    converter = VideoConverter()
    print(converter.convert("test.mp4", "mp4"))
    print(converter.convert("test.ogg", "ogg"))
