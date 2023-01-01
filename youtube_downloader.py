from pytube import YouTube


def get_video():
    url = input('Enter youtube video url to download: ')

    def on_progress(stream, chunk, bytes_remaining):
        """On process callback function"""
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        pct_completed = bytes_downloaded / total_size * 100
        print(f"Status: {round(pct_completed, 2)} %")

    def on_complete(stream, output_path):
        """On complete callback function"""
        total_size = stream.filesize
        size_mb = round(total_size / (1024 * 1024), 2)
        print(f"Download Completed: {size_mb} mb")
        print(f'Path: {output_path}')

    yt = YouTube(url,
                 on_progress_callback=on_progress,
                 on_complete_callback=on_complete)

    print(f'Downloading: {yt.title}')

    yt.streams.filter().get_highest_resolution().download()

    print('Download finished.')
