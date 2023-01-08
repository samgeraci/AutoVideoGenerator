from moviepy.editor import *


def edit_clip(number_of_sentences):
    clips = []
    for i in range(number_of_sentences):
        audio_file_name = "audio" + str(i) + ".mp3"
        sentence_audio = AudioFileClip(audio_file_name)
        clip = ImageClip(img="screenshot" + str(i) + ".png", duration=sentence_audio.duration)
        clip = clip.set_audio(sentence_audio)
        clips.append(clip)
    final_clip = concatenate_videoclips(clips)
    final_clip.set_fps(fps=24)
    final_clip.write_videofile(filename="final_video.mp4", fps=24)
