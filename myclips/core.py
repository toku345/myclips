#!/usr/bin/env python3
import os
import subprocess
import requests

SLACK_FILES_UPLOAD_URL = "https://slack.com/api/files.upload"


def generate_filename(now):
    timestamp = now.strftime("%Y-%m-%d_%H_%M_%S")
    filename = "%s%s" % (timestamp, ".h264")
    return os.path.join("/home/pi/Pictures", filename)


def h264_to_mp4(input_file_path):
    input_file_name, _ = os.path.basename(input_file_path).split(".")
    output_dir = os.path.dirname(input_file_path)
    output_file_path = os.path.join(output_dir, input_file_name + ".mp4")

    try:
        subprocess.run(["MP4Box", "-add", input_file_path, output_file_path],
                       check=True)
    except subprocess.CalledProcessError:
        return None
    else:
        return output_file_path


def upload_video_to_slack(input_file_path, slack_token, channel_id):
    params = {
        "token": slack_token,
        "channels": channel_id
    }
    files = {
        "file": open(input_file_path, 'rb')
    }
    requests.post(url=SLACK_FILES_UPLOAD_URL, params=params, files=files)
