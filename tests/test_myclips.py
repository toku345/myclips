import datetime

from myclips.core import generate_filename


def test_generate_filename():
    now = datetime.datetime(2019, 1, 23, 12, 34, 56)
    expected = "/home/pi/Pictures/2019-01-23_12.34.56.h264"
    assert generate_filename(now) == expected
