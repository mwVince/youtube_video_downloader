from pytube import YouTube


def get_video():
    url = input('Enter youtube video url to download: ')

    def on_progress(stream, chunk, bytes_remaining):
        """On process callback function"""
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        pct_completed = bytes_downloaded / total_size * 100
        print(f"Status: {round(pct_completed, 2)} %")

    yt = YouTube(url, on_progress_callback=on_progress)

    print(f'Downloading: {yt.title}')

    yt.streams.filter().get_highest_resolution().download()

    print('Download finished.')
