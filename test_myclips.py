import myclips
import datetime
from unittest import mock

def test_generate_filename():
    now = datetime.datetime(2019, 1, 23, 12, 34, 56)
    assert myclips.generate_filename(now) == "2019-01-23_12.34.56.jpg"
