#!/usr/bin/env python3
import os


def generate_filename(now):
    timestamp = now.strftime("%Y-%m-%d_%H.%M.%S")
    filename = "%s%s" % (timestamp, ".h264")
    return os.path.join("/home/pi/Pictures", filename)
