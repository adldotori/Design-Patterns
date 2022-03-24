from abc import ABC, abstractmethod


class ThirdPartyYoutubeLib(ABC):
    def __init__(self):
        self.download_count = 0

    @abstractmethod
    def list_videos(self, video):
        raise NotImplementedError

    @abstractmethod
    def download_video(self, id):
        raise NotImplementedError

    def get_download_count(self):
        return self.download_count


class ThirdPartyYoutube(ThirdPartyYoutubeLib):
    DB = {}

    def list_videos(self):
        return self.DB

    def download_video(self, id):
        self.DB[id] = "video" + str(id)
        self.download_count += 1
        print("Downloading... It works takes an hour")
        return self.DB[id]


class CachedYoutube(ThirdPartyYoutubeLib):
    video_cache = {}

    def __init__(self, service: ThirdPartyYoutube):
        super().__init__()
        self.service = service

    def list_videos(self):
        return self.service.list_videos()

    def download_video(self, id):
        if id in self.video_cache:
            return self.video_cache[id]
        else:
            video = self.service.download_video(id)
            self.video_cache[id] = video
            return video

    def get_download_count(self):
        return self.service.get_download_count()
