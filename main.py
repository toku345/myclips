#!/usr/bin/env python3
import datetime
from time import sleep

from picamera import PiCamera

from aiy.vision.inference import CameraInference
from aiy.vision.models import face_detection

from myclips.core import generate_filename, h264_to_mp4


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

                    h264_to_mp4(h264_file_path)

                    sleep(1)


if __name__ == '__main__':
    print("script start!")
    main()
