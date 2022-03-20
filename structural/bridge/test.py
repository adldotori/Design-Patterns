from device import TV, Radio, Device
from remote import Remote, AdvancedRemote


class Test(object):
    def test_tv_volume(self):
        tv: Device = TV()
        remote = Remote(tv)
        remote.toggle_power()
        remote.volume_up()
        assert tv.volume == 1
        remote.volume_down()
        assert tv.volume == 0

    def test_tv_channel(self):
        tv: Device = TV()
        remote = Remote(tv)
        remote.toggle_power()
        remote.volume_up()
        assert tv.volume == 1
        remote.volume_down()
        assert tv.volume == 0

    def test_mute(self):
        radio: Device = Radio()
        remote = AdvancedRemote(radio)
        remote.toggle_power()
        remote.volume_up()
        assert radio.volume == 1
        remote.volume_down()
        assert radio.volume == 0
        remote.mute()
        assert radio.volume == 0
