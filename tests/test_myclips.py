import pytest

import datetime
import os
import requests

from myclips import core
from myclips.core import (generate_filename, h264_to_mp4,
                          upload_video_to_slack, SLACK_FILES_UPLOAD_URL)


def test_generate_filename():
    now = datetime.datetime(2019, 1, 23, 12, 34, 56)
    expected = "/home/pi/Pictures/2019-01-23_12_34_56.h264"
    assert generate_filename(now) == expected


@pytest.fixture
def dummy_file_cleaner():
    output_file_path = "./tests/fixtures/files/dummy.mp4"

    if os.path.exists(output_file_path):
        print("remove file:", output_file_path)
        os.remove(output_file_path)

    yield

    if os.path.exists(output_file_path):
        print("remove file:", output_file_path)
        os.remove(output_file_path)


def test_h264_to_mp4(dummy_file_cleaner):
    input_file_path = "./tests/fixtures/files/dummy.h264"
    output_file_path = "./tests/fixtures/files/dummy.mp4"
    assert h264_to_mp4(input_file_path) == output_file_path
    assert os.path.exists(output_file_path)


def test_h264_to_mp4_empty_file():
    input_file_path = "./tests/fixtures/files/empty.h264"
    output_file_path = "./tests/fixtures/files/empty.mp4"
    assert h264_to_mp4(input_file_path) is None
    assert not os.path.exists(output_file_path)


def test_post_to_slack(mocker):
    input_file_path = "/home/pi/Pictures/2019-01-23_12_34_56.h264"

    mocker.patch("requests.post")

    mock_file = mocker.mock_open()
    mocker.patch.object(core, "open", mocker.Mock(return_value=mock_file))
    upload_video_to_slack(input_file_path, "dummy token", "dummy channel")

    expected_params = {
        "token": "dummy token",
        "channels": "dummy channel"
    }
    expected_files = {
        "file": mock_file
    }
    core.open.assert_called_once_with(input_file_path, 'rb')
    requests.post.assert_called_once_with(url=SLACK_FILES_UPLOAD_URL,
                                          params=expected_params,
                                          files=expected_files)
