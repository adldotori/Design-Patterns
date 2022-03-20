from device import TV, Radio
from remote import Remote, AdvancedRemote

if __name__ == "__main__":
    tv = TV()
    remote = Remote(tv)
    remote.toggle_power()
    remote.volume_up()
    remote.volume_down()
    remote.channel_up()
    remote.channel_down()

    radio = Radio()
    remote = AdvancedRemote(radio)
    remote.toggle_power()
    remote.volume_up()
    remote.volume_down()
    remote.channel_up()
    remote.channel_down()
    remote.mute()
    remote.volume_up()
