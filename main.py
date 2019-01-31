#!/usr/bin/env python3
import datetime
from time import sleep

from picamera import PiCamera

from aiy.vision.inference import CameraInference
from aiy.vision.models import face_detection

from myclips.core import generate_filename


def main():
    with PiCamera(resolution=(1640, 922)) as camera:
        with CameraInference(face_detection.model()) as inference:
            for result in inference.run():
                if len(face_detection.get_faces(result)) >= 1:
                    print("face detected!")
                    video_file = generate_filename(datetime.datetime.now())
                    camera.start_recording(video_file, format='h264')
                    sleep(5)
                    camera.stop_recording()


if __name__ == '__main__':
    print("script start!")
    main()
