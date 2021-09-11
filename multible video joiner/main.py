from moviepy.editor import VideoFileClip, concatenate_videoclips
import time
from colorama import Style, Fore
import os


def clear():
    os.system('cls||clear')


START_TIME = time.time()
clear()
CURRENT_DIR = os.path.dirname(__file__)
video_formats = ['mp4', 'mkv']  # you can add whatever video format you want
OUTPUT_VIDEO_NAME = os.path.basename(CURRENT_DIR)
print(f'{Fore.GREEN}[*]{Style.RESET_ALL} Script Started..')
clear()
print(
    f'{Fore.GREEN}[/] {Style.RESET_ALL}The Working Directory is : {CURRENT_DIR}')


def get_videos():
    videos = []
    all_files = os.listdir(CURRENT_DIR)

    for file in all_files:
        if file.split('.')[-1].strip() in video_formats and os.path.isfile(file):
            video_file_full_path = os.path.join(CURRENT_DIR, file)
            videos.append(video_file_full_path)
    print(f'[*] Found {len(videos)} Videos ')
    return videos


def concat(videos: list):
    video_objects = []
    for index, video in enumerate(videos):
        print(
            f'[-] Making Video Object {index+1} from {len(videos)}', end='\r')
        clip = VideoFileClip(video)
        video_objects.append(clip)
    final_video = concatenate_videoclips(video_objects)
    clear()
    print(f'[+] Writing The Final Video into :"{OUTPUT_VIDEO_NAME}.mp4"')
    final_video.write_videofile(os.path.join(
        CURRENT_DIR, f'{OUTPUT_VIDEO_NAME}.mp4'))


videos = get_videos()
concat(videos)
END_TIME = time.time()
print(
    f'{Style.BRIGHT}{Fore.BLUE}[*]{Fore.RESET} The process finished in {round(END_TIME-START_TIME)} seconds {Style.BRIGHT}')
