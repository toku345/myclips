#!/usr/bin/env python3
import datetime
from time import sleep
import os

from picamera import PiCamera

from aiy.vision.inference import CameraInference
from aiy.vision.models import face_detection

from myclips.core import (generate_filename, h264_to_mp4,
                          upload_video_to_slack)

SLACK_TOKEN = os.getenv('SLACK_TOKEN')
SLACK_CHANNEL_ID = os.getenv('SLACK_CHANNEL_ID')


def main():
    with PiCamera(resolution=(1640, 922)) as camera:
        with CameraInference(face_detection.model()) as inference:
            for result in inference.run():
                if len(face_detection.get_faces(result)) >= 1:
                    print("face detected!")
                    h264_file_path = generate_filename(datetime.datetime.now())

                    camera.start_recording(h264_file_path, format='h264')
                    sleep(5)
                    camera.stop_recording()

                    output_file_path = h264_to_mp4(h264_file_path)

                    upload_video_to_slack(output_file_path, SLACK_TOKEN,
                                          SLACK_CHANNEL_ID)


if __name__ == '__main__':
    print("script start!")
    main()
