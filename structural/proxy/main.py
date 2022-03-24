from youtube import CachedYoutube, ThirdPartyYoutube

if __name__ == "__main__":
    youtube = CachedYoutube(ThirdPartyYoutube())
    youtube.download_video(1)
    youtube.download_video(2)
    youtube.download_video(3)
    youtube.list_videos()
    youtube.download_video(3)
    youtube.download_video(4)

    print("-" * 20)
    youtube = ThirdPartyYoutube()
    youtube.download_video(1)
    youtube.download_video(2)
    youtube.download_video(3)
    youtube.list_videos()
    youtube.download_video(3)
    youtube.download_video(4)
