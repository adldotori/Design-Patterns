from device import Device


class Remote(object):
    def __init__(self, device, log=False):
        self.device = device
        self.log = log

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_up(self):
        self.device.volume = self.device.volume + 1
        if self.log:
            print(f"Volume: {self.device.volume}")

    def volume_down(self):
        self.device.volume = self.device.volume - 1
        if self.log:
            print(f"Volume: {self.device.volume}")

    def channel_up(self):
        self.device.channel = self.device.channel + 1
        if self.log:
            print(f"Channel: {self.device.channel}")

    def channel_down(self):
        self.device.channel = self.device.channel - 1
        if self.log:
            print(f"Channel: {self.device.channel}")


class AdvancedRemote(Remote):
    def mute(self):
        self.device.volume = 0
