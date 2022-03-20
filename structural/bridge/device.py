class Device(object):
    def __init__(self):
        self._is_on = False
        self._volume = 0
        self._channel = 0

    def is_enabled(self):
        return self._is_on

    def enable(self):
        self._is_on = True

    def disable(self):
        self._is_on = False

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self._volume = volume

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel):
        self._channel = channel


class TV(Device):
    pass


class Radio(Device):
    pass
