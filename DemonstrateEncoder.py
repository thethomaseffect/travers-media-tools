""" Main Method to demonstrate Encoder easily"""
from Encoders import Encoder
import time

PATH_TO_QUEUE = '/home/thomas/encodeQueue/'
PATH_TO_FINISHED = '/home/thomas/encodeQueue/finishedJobs/'

INPUT_PATH = PATH_TO_QUEUE + 'input.mp4'
OUTPUT_PATH = PATH_TO_FINISHED + 'output.mkv'


def main():
    """Runs the encoder on the files specified by inputPath and outputPath."""
    video_encoder = Encoder(INPUT_PATH, OUTPUT_PATH)
    video_encoder.start()
    while video_encoder.alive():
        print(video_encoder.get_time_elapsed())
        time.sleep(0.1)

if __name__ == '__main__':
    main()
