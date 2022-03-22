class VideoFile(object):
    def __init__(self, file):
        self.file = file


class OggCompressionCodec(object):
    pass


class MPEG4CompressionCodec(object):
    pass


class CodecFactory(object):
    def __init__(self, file):
        self.file = file


class BitrateReader(object):
    def read(file, codec):
        pass

    def convert(buffer, codec):
        pass


class AudioMixer(object):
    def mix(self, result):
        return "It's AudioMixer"


class VideoConverter(object):
    def convert(self, filename, format):
        file = VideoFile(filename)
        source_codec = CodecFactory(file)
        if format == "mp4":
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()
        buffer = BitrateReader.read(file, source_codec)
        result = BitrateReader.convert(buffer, destination_codec)
        result = AudioMixer().mix(result)
        return result
