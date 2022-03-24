from youtube import CachedYoutube, ThirdPartyYoutube


def test_cached_youtube():
    youtube = CachedYoutube(ThirdPartyYoutube())
    youtube.download_video(1)
    youtube.download_video(2)
    youtube.download_video(3)
    youtube.list_videos()
    youtube.download_video(3)
    youtube.download_video(4)

    assert youtube.get_download_count() == 4


def test_third_party_youtube():
    youtube = ThirdPartyYoutube()
    youtube.download_video(1)
    youtube.download_video(2)
    youtube.download_video(3)
    youtube.list_videos()
    youtube.download_video(3)
    youtube.download_video(4)

    assert youtube.get_download_count() == 5
