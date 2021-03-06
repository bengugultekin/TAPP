import os
from kivy.app import App
from kivy.clock import Clock
from pytube import YouTube
from kivy.lang import Builder
# from kivy import Platform
import pytube
from kivy.clock import Clock



kv = Builder.load_file('main.kv')

class MyApp(App):
    image_loaded = False


    def build(self):
        self.title = " TubeApp Video Downloader"
        return kv

    def set_assets(self ,thumbnail , title):
        self.root.ids.thumbnail.source = thumbnail
        self.root.ids.title.text = title


    def get_video(self,stream):
        stream.download()

    def get_video_info(self,url):
        try:
            yt = pytube.YouTube(url)
            self.set_assets(yt.thumbnail_url,yt.title)
            self.image_loaded = True
            Clock.schedule_once(lambda x: self.get_video(yt.streams.get_highest_resolution()),4)
            print('Video indirmeniz başlatıldı..')
        except:
            print("Hatalı video linki!")
    def get_mp3_info(self,url):
        try:
            yt=pytube.YouTube(url)
            self.set_assets(yt.thumbnail_url,yt.title)
            self.image_loaded = True

            Clock.schedule_once(lambda x: self.get_video(yt.streams.get_audio_only()),3)
            print('Ses dosyası indirmeniz başladı..')
        except:
            print("Bir hata meydana geldi!")

if __name__=="__main__":
    MyApp().run()