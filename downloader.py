from pytubefix import YouTube
import os
#made for personal use so i wont have to deal with sketchy sites
def ytviddownloader(url, save_path=None):
    try:
        # If no path provided → use Windows Videos folder
        if save_path is None:
            save_path = os.path.join(os.path.expanduser("~"), "Videos")

        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()

        print(f"Downloading: {yt.title}")
        stream.download(output_path=save_path)
        print(f"Downloaded to: {save_path}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ").strip()
    ytviddownloader(video_url)
