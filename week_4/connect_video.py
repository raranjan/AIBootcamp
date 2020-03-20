import cv2
from logzero import logger
import os

logger.info("OpenCV version -- {}".format(cv2.__version__))

PATH = "../data/video_combine/"

height = 720
width = 1280

# Iterate through the
files = [item for item in os.listdir(PATH) if item[-4:]=='.mp4' in item]
[logger.info("File - {}: {}".format(i+1, item)) for i, item in enumerate(files)]

def combine_video_files():
    video_index = 0
    cap = cv2.VideoCapture(PATH + files[video_index])

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(PATH + 'output.mp4', fourcc, 20, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if frame is None:
            logger.info("End of video {} .... next one now".format(video_index))
            video_index += 1
            if video_index >= len(files):
                break

            cap = cv2.VideoCapture(PATH + files[video_index])
            ret, frame = cap.read()
        out.write(frame)

    cap.release()
    out.release()
    logger.info("End")

if __name__ == '__main__':
    combine_video_files()