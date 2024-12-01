import os
from moviepy import VideoFileClip, concatenate_videoclips
from pydub import AudioSegment

ONLINE_FILES_PATH = "data/online_files"
OUTPUT_PATH = "output"


mp4_file_list = []
for item in os.listdir(ONLINE_FILES_PATH):
    item_path = os.path.join(ONLINE_FILES_PATH, item)
    if os.path.isdir(item_path):
        if os.path.exists(os.path.join(ONLINE_FILES_PATH, f"{item}.mp4")):
            continue
        mp4_clips = []
        for sub_item in sorted(os.listdir(item_path)):
            sub_item_path = os.path.join(item_path, sub_item)
            if sub_item.endswith('.mp4'):
                mp4_clips.append(VideoFileClip(sub_item_path))
        if mp4_clips:
            # Concatenate and save as the folder name
            combined_clip = concatenate_videoclips(mp4_clips)
            output_path = os.path.join(ONLINE_FILES_PATH, f"{item}.mp4")
            combined_clip.write_videofile(output_path, codec="libx264")
            combined_clip.close()
            mp4_clips = [clip.close() for clip in mp4_clips]  # Close all clips after use
            mp4_file_list.append(f"{item}.mp4")
    elif item.endswith('.mp4'):
        mp4_file_list.append(item)

for file in mp4_file_list:
    print(f"Processing {file}")

    video_clip = VideoFileClip(os.path.join(ONLINE_FILES_PATH, file))
    audio_clip = video_clip.audio
    output_audio_path = os.path.join(OUTPUT_PATH, f"{file[:-4]}.wav")
    audio_clip.write_audiofile(output_audio_path)
    audio_clip.close()
    video_clip.close()

    audio = AudioSegment.from_file(output_audio_path)
    audio = audio.set_frame_rate(16000).set_sample_width(2)  # 16-bit = 2 bytes per sample
    audio.export(output_audio_path, format="wav")

    print(f"Audio extracted and saved as {output_audio_path}")
