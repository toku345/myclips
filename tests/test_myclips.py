import myclips.main
import datetime

def test_generate_filename():
    now = datetime.datetime(2019, 1, 23, 12, 34, 56)
    assert myclips.main.generate_filename(now) == "2019-01-23_12.34.56.jpg"
