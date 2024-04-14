""" Yuse Logic Component
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.03.01(0700) """

import math
import os
import moviepy
from moviepy.editor import VideoFileClip


class Editor:
    def __init__(self):
        self.videos = self.get_videos()
        self.digits = 3
        try:
            with open("part.dat") as file:
                self.part_number = int(file.read())

        except FileNotFoundError:
            self.part_number = 000
        finally:
            self.title = f"Final Fantasy VII Rebirth File# {str(self.part_number).zfill(self.digits)}.mp4"
            self.full_video = ""
            self.default_start = 0
            self.default_length = 1200
            self.start = 0
            self.length = 1200
            # self.clips = []
            # self.clip_number = 0
            # self.total_clips = 0

    @staticmethod
    def get_videos():
        items = os.listdir("Input")
        items.remove("Intro")
        items.remove("Outro")
        return items

    def get_clips(self):
        for item in self.videos:
            self.full_video = f"Input/{item}"
            self.start = self.default_start
            self.length = self.default_length
            clips = []
            current_duration = VideoFileClip(self.full_video).duration
            clip_number = current_duration/self.length
            while round(clip_number) > 0:
                clip = (self.start, self.length)
                clips.append(clip)
                self.start += self.default_length
                self.length += self.default_length
                clip_number -= 1

                if round(clip_number) == 0:
                    self.start = self.length - 1200
                    clip_difference = abs(self.start-current_duration)
                    clip_length = self.start + math.floor(clip_difference)
                    clip = (self.start, clip_length)
                    clips.append(clip)

            total_clips = len(clips)
            print(f"{item} has {total_clips} clips to be processed!\n{clips}")
            self.make_clips(clips)
            print(f"Success all {total_clips} of {item}'s clips have been processed!")

    def make_clips(self, clips):
        while clips:
            main_video = VideoFileClip(self.full_video)
            vid_start = clips[0][0]
            vid_end = clips[0][1]
            clipped = main_video.subclip(vid_start, vid_end)
            current_video = f"Output/Final Fantasy VII Rebirth File# {str(self.part_number).zfill(self.digits)}.mp4"
            clipped.to_videofile(current_video, codec="libx264", temp_audiofile='temp-audio.m4a',
                                 remove_temp=True, audio_codec='aac')
            self.part_number += 1
            clips.pop(0)

            print("-----------------###-----------------")

            with open('part.dat', 'w+') as file:
                file.write(str(self.part_number).zfill(self.digits))
                file.close()
