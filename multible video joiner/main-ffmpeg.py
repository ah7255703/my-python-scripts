import ffmpeg
import os


CURRENT_DIR = os.path.dirname(__file__)
video_formats = ['mp4', 'mkv', 'mov']
OUTPUT_VIDEO_NAME = os.path.basename(CURRENT_DIR)


def clear():
    os.system('cls||clear')


def get_videos():
    videos = []
    all_files = os.listdir(CURRENT_DIR)

    for file in all_files:
        if file.split('.')[-1].strip() in video_formats and os.path.isfile(file):
            video_file_full_path = os.path.join(CURRENT_DIR, file)
            videos.append(video_file_full_path)
    print(f'[*] Found {len(videos)} Videos ')
    return videos


def concat(videos):
    videos_objs = []
    for video in videos:
        video_obj = ffmpeg.input(video)
        videos_objs.append(video_obj)
    concated_objs = ffmpeg.concat(*videos_objs)
    out = ffmpeg.output(
        concated_objs, f'{CURRENT_DIR}/{OUTPUT_VIDEO_NAME}.mp4').run()


videos = get_videos()
concat(videos)
