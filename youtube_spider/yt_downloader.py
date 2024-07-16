from pytube import YouTube
from pytube.innertube import _default_clients
from extract_audio_from_video import extract_audio_customized


_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]


vid_title = ""


def format_vid_title():
    global vid_title
    if " " in vid_title:
        vid_title = vid_title.strip().replace(" ", "")
    if "/" in vid_title:
        vid_title = vid_title.replace("/", "")


# Function to download YouTube video
def download_youtube_video(url, output_path='.'):
    global vid_title
    try:
        # Create a YouTube object with the URL
        yt = YouTube(url,
                     use_oauth=False,
                     allow_oauth_cache=True
                     )

        # Print video title
        print(f"Title: {yt.title}")
        vid_title = yt.title
        format_vid_title()

        # Get the highest resolution stream
        ys = yt.streams.get_highest_resolution()

        # Print the download start message
        print("Downloading...")

        # Download the video
        ys.download(output_path, filename="./mp4/" + vid_title + ".mp4")

        # Print download completion message
        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")


def get_audio_path(vid_path: str):
    # i = vid_path.rfind(".")
    return vid_path + ".mp3"


# Example usage
if __name__ == "__main__":
    # vid_output_path = "./"
    video_url = 'https://www.youtube.com/watch?v=rdccTOcX7o4'  # Replace with your video URL
    download_youtube_video(video_url)
    # extrac the audio from the video
    print("\nExtracting the audio from the video ...")
    aud_input_path = vid_title
    aud_output_path = get_audio_path(aud_input_path)
    # print("audio path: ", aud_output_path)
    aud_input_path = "./mp4/" + vid_title + ".mp4"
    extract_audio_customized(aud_input_path, "./mp3/" + aud_output_path)


"""
# .../site-packages/pytube/request.py
# I have changed this module at line 38 by adding context:
# return urlopen(request, timeout=timeout, context=ssl.SSLContext())
"""

