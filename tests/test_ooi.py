"""Unit tests for OOI workflow"""
import datetime
import os.path

import pytest

from ooi_processing import save_ooi_spectrograms


@pytest.mark.parametrize(
    "start_time_str, end_time_str, segment_length, node, output_dir, expected_files_count",
    [
        ("2017-03-10T00-00-00", "2017-03-10T00-05-00", None, None, None, 1),
        ("2017-03-10T00-00-00", "2017-03-10T00-05-00", 1, None, None, 5),
        ("2017-03-10T00-00-00", "2017-03-10T00-05-00", 1, None, "long/path/", 5),
    ],
)
def test_ooi_spectrograms(
    start_time_str, end_time_str, segment_length, node, output_dir, expected_files_count
):
    start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%dT%H-%M-%S")
    end_time = datetime.datetime.strptime(end_time_str, "%Y-%m-%dT%H-%M-%S")
    save_ooi_spectrograms(start_time, end_time, segment_length, node, output_dir)
    assert expected_files_count == len(
        [name for name in os.listdir(output_dir) if os.path.isfile(name)]
    )
