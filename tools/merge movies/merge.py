
import moviepy.editor as mp

# Load the video files
video_files = [
    "out.mp4",
    "out (1).mp4",
    "out (2).mp4",
    "out (3).mp4"
]

# Load the video clips
video_clips = [mp.VideoFileClip(file) for file in video_files]

# Concatenate the videos
final_video = mp.concatenate_videoclips(video_clips)

# Write the result to a new file
output_path = "merged_video_final.mp4"
final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
