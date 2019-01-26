import time


def generate_filename(now):
    timestamp = now.strftime("%Y-%m-%d_%H.%M.%S")
    return "%s%s" % (timestamp, ".jpg")
