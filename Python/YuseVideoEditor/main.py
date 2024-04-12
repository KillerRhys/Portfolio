import math
from moviepy.editor import VideoFileClip


# Setup video & Numbers
full_video = 'Videos/#19.mp4'
digits = 3
with open("part.dat") as file:
    part_number = int(file.read())
current_duration = VideoFileClip(full_video).duration
clip_start = 0
clip_length = 1200
clips = []
clip_number = current_duration/clip_length
while round(clip_number) > 0:
    clip_start = clip_start
    clip_length = clip_length
    clip = (clip_start, clip_length)
    clips.append(clip)
    clip_start += 1200
    clip_length += 1200
    clip_number -= 1

    if round(clip_number) == 0:
        clip_start = clip_length - 1200
        clip_difference = abs(clip_start-current_duration)
        clip_length = clip_start + math.floor(clip_difference)
        clip = (clip_start, clip_length)
        clips.append(clip)

total_clips = len(clips)
print(f"{total_clips} clips to be processed!\n{clips}")

print(clips)

current_video = f"Final Fantasy VII Rebirth File# {str(part_number).zfill(digits)}.mp4"
print(current_video)


while clips:
    main_video = VideoFileClip(full_video)
    vid_start = clips[0][0]
    vid_end = clips[0][1]
    clipped = main_video.subclip(vid_start, vid_end)
    current_video = f"Final Fantasy VII Rebirth File# {str(part_number).zfill(digits)}.mp4"
    clipped.to_videofile(current_video, codec="libx264", temp_audiofile='temp-audio.m4a',
                         remove_temp=True, audio_codec='aac')
    part_number += 1
    clips.pop(0)

    print("-----------------###-----------------")

    with open('part.dat', 'w+') as file:
        file.write(str(part_number).zfill(digits))
        file.close()


print(f"Success all {total_clips} clips have been processed!")
