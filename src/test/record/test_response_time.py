# Copyright 2021 Research Institute of Systems Planning, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from caret_analyze.exceptions import InvalidRecordsError
from caret_analyze.record.record_factory import RecordFactory, RecordsFactory
from caret_analyze.record.response_time import ResponseTime

import pytest


def create_records(records_raw, columns):
    records = RecordsFactory.create_instance()
    for column in columns:
        records.append_column(column, [])

    for record_raw in records_raw:
        record = RecordFactory.create_instance(record_raw)
        records.append(record)
    return records


def to_dict(records):
    return [record.data for record in records]


def check(records_raw, expect_raw, columns):
    records = create_records(records_raw, columns)
    response = ResponseTime(records, columns[0], columns[-1]).to_records()
    d = to_dict(response)
    assert d == expect_raw


class TestResponseRecords:

    def test_empty_flow_case(self):
        records_raw = [
        ]
        columns = ['start', 'end']

        records = create_records(records_raw, columns)
        response = ResponseTime(records, columns[0], columns[1])

        expect_raw = []
        result = to_dict(response.to_records())
        assert result == expect_raw

        expect_raw = []
        result = to_dict(response.to_response_records())
        assert result == expect_raw

        expect_raw = []
        assert to_dict(response.to_records(all_pattern=True)) == expect_raw

    def test_single_flow_case(self):
        records_raw = [
            {'start': 0, 'end': 1},
        ]
        columns = ['start', 'end']

        records = create_records(records_raw, columns)
        response = ResponseTime(records, columns[0], columns[1])

        expect_raw = [
        ]
        result = to_dict(response.to_records())
        assert result == expect_raw

        expect_raw = [
        ]
        result = to_dict(response.to_response_records())
        assert result == expect_raw

        expect_raw = [
            {'start': 0, 'end': 1}
        ]
        assert to_dict(response.to_records(all_pattern=True)) == expect_raw

    def test_double_flow_case(self):
        records_raw = [
            {'start': 0, 'end': 1},
            {'start': 2, 'end': 3},
        ]
        columns = ['start', 'end']

        records = create_records(records_raw, columns)
        response = ResponseTime(records, columns[0], columns[1])

        expect_raw = [
            {'start': 0, 'end': 3},
            {'start': 2, 'end': 3},
        ]
        result = to_dict(response.to_records())
        assert result == expect_raw

        expect_raw = [
            {'start_min': 0, 'start_max': 2, 'end': 3},
        ]
        result = to_dict(response.to_response_records())
        assert result == expect_raw

        expect_raw = [
            {'start': 0, 'end': 1},
            {'start': 0, 'end': 3},
            {'start': 2, 'end': 3},
        ]
        assert to_dict(response.to_records(all_pattern=True)) == expect_raw

    def test_cross_flow_case(self):
        records_raw = [
            {'start': 0, 'end': 10},
            {'start': 3, 'end': 4},
            {'start': 4, 'end': 8},
            {'start': 6, 'end': 6},
        ]
        columns = ['start', 'end']

        records = create_records(records_raw, columns)
        response = ResponseTime(records, columns[0], columns[1])

        expect_raw = [
            {'start': 0, 'end': 4},
            {'start': 3, 'end': 4},
            {'start': 3, 'end': 6},
            {'start': 6, 'end': 6},
        ]
        result = to_dict(response.to_records())
        assert result == expect_raw

        expect_raw = [
            {'start_min': 0, 'start_max': 3, 'end': 4},
            {'start_min': 3, 'start_max': 6, 'end': 6},
        ]
        result = to_dict(response.to_response_records())
        assert result == expect_raw

        expect_raw = [
            {'start': 0, 'end': 4},
            {'start': 0, 'end': 6},
            {'start': 0, 'end': 8},
            {'start': 0, 'end': 10},
            {'start': 3, 'end': 4},
            {'start': 4, 'end': 8},
            {'start': 6, 'end': 6},
        ]
        result = to_dict(response.to_records(all_pattern=True))
        assert result == expect_raw

    def test_triple_flow_case(self):
        records_raw = [
            {'start': 0, 'end': 1},
            {'start': 2, 'end': 3},
            {'start': 10, 'end': 11},
        ]
        columns = ['start', 'end']

        records = create_records(records_raw, columns)
        response = ResponseTime(records, columns[0], columns[1])

        expect_raw = [
            {'start': 0, 'end': 3},
            {'start': 2, 'end': 3},
            {'start': 2, 'end': 11},
            {'start': 10, 'end': 11}
        ]
        result = to_dict(response.to_records())
        assert result == expect_raw

        expect_raw = [
            {'start_min': 0, 'start_max': 2, 'end': 3},
            {'start_min': 2, 'start_max': 10, 'end': 11},
        ]
        result = to_dict(response.to_response_records())
        assert result == expect_raw

        expect_raw = [
            {'start': 0, 'end': 1},
            {'start': 0, 'end': 3},
            {'start': 2, 'end': 3},
            {'start': 2, 'end': 11},
            {'start': 10, 'end': 11},
        ]

        result = to_dict(response.to_records(all_pattern=True))
        assert result == expect_raw

    def test_double_flow_cross_case(self):
        records_raw = [
            {'start': 0, 'end': 5},
            {'start': 2, 'end': 3},
        ]
        columns = ['start', 'end']

        records = create_records(records_raw, columns)
        response = ResponseTime(records, columns[0], columns[1])

        expect_raw = [
            {'start': 0, 'end': 3},
            {'start': 2, 'end': 3}
        ]
        result = to_dict(response.to_records())
        assert result == expect_raw

        expect_raw = [
            {'start_min': 0, 'start_max': 2, 'end': 3},
        ]
        result = to_dict(response.to_response_records())
        assert result == expect_raw

        expect_raw = [
            {'start': 0, 'end': 3},
            {'start': 0, 'end': 5},
            {'start': 2, 'end': 3},
        ]

        result = to_dict(response.to_records(all_pattern=True))
        assert result == expect_raw


class TestResponseHistogram:

    def test_empty(self):
        records_raw = [
        ]
        columns = ['start', 'end']

        records = create_records(records_raw, columns)
        response = ResponseTime(records, columns[0], columns[1])

        with pytest.raises(InvalidRecordsError):
            response.to_histogram()

    def test_single_flow_case(self):
        records_raw = [
            {'start': 0, 'end': 1},
        ]
        columns = ['start', 'end']

        records = create_records(records_raw, columns)
        response = ResponseTime(records, columns[0], columns[1])

        with pytest.raises(InvalidRecordsError):
            response.to_histogram()

    def test_double_flow_case(self):
        records_raw = [
            {'start': 0, 'end': 1},
            {'start': 2, 'end': 3},
        ]
        columns = ['start', 'end']

        records = create_records(records_raw, columns)
        response = ResponseTime(records, columns[0], columns[1])

        hist, latency = response.to_histogram(1)
        assert list(hist) == [1, 2]
        assert list(latency) == [1, 2, 3]

    def test_cross_flow_case(self):
        records_raw = [
            {'start': 0, 'end': 10},
            {'start': 3, 'end': 4},
            {'start': 4, 'end': 8},
            {'start': 6, 'end': 6},
        ]
        columns = ['start', 'end']

        records = create_records(records_raw, columns)
        response = ResponseTime(records, columns[0], columns[1])

        hist, latency = response.to_histogram(1)
        assert list(hist) == [1, 2, 2, 3]
        assert list(latency) == [0, 1, 2, 3, 4]

    def test_triple_flow_case(self):
        records_raw = [
            {'start': 0, 'end': 1},
            {'start': 2, 'end': 3},
            {'start': 10, 'end': 11},
        ]
        columns = ['start', 'end']

        records = create_records(records_raw, columns)
        response = ResponseTime(records, columns[0], columns[1])

        hist, latency = response.to_histogram(1)
        assert list(hist) == [2, 2, 2, 1, 1, 1, 1, 2]
        assert list(latency) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_double_flow_cross_case(self):
        records_raw = [
            {'start': 0, 'end': 5},
            {'start': 2, 'end': 3},
        ]
        columns = ['start', 'end']

        records = create_records(records_raw, columns)
        response = ResponseTime(records, columns[0], columns[1])

        hist, latency = response.to_histogram(1)
        assert list(hist) == [1, 2]
        assert list(latency) == [1, 2, 3]
