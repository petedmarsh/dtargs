# -*- coding: utf-8 -*-

from datetime import date, datetime
import argparse
import dtargs
import mock
import pytest
import pytz


class TestDateType:

    def test_no_format_specified(self):
        assert dtargs.DateType().date_format == '%Y-%m-%d'

    def test_format_specified(self):
        date_format = '%d/%m/%Y'
        assert dtargs.DateType(date_format).date_format == date_format

    def test_repr(self):
        dt = dtargs.DateType()
        assert repr(dt) == 'DateType(date_format="%s")' % dt.date_format

    def test_default_format_call_with_correctly_formatted_date(self):
        dt = dtargs.DateType()
        date_string = '2015-01-02'
        assert dt(date_string) == date(2015, 1, 2)

    def test_default_format_call_with_incorrectly_formatted_date(self):
        with pytest.raises(argparse.ArgumentTypeError):
            dt = dtargs.DateType()
            date_string = '01/02/2015'
            dt(date_string)

    def test_call_with_none(self):
        with pytest.raises(argparse.ArgumentTypeError):
            dt = dtargs.DateType()
            dt(None)

    def test_custom_format_call_with_correctly_formatted_date(self):
        dt = dtargs.DateType('%d/%m/%Y')
        date_string = '01/02/2015'
        assert dt(date_string) == date(2015, 2, 1)

    def test_custom_format_call_with_incorrectly_formatted_date(self):
        with pytest.raises(argparse.ArgumentTypeError):
            dt = dtargs.DateType('%d/%m/%Y')
            date_string = '2015-01-02'
            dt(date_string)


class TestDateTime:

    def test_no_format_specified(self):
        assert dtargs.DateTimeType().date_time_format == '%Y-%m-%dT%H:%M:%SZ'

    def test_no_timezone_specified(self):
        assert dtargs.DateTimeType().tz == pytz.utc

    def test_repr(self):
        dtt = dtargs.DateTimeType()
        assert repr(dtt) == 'DateTimeType(date_time_format="%s", tz=%s)' % (
            dtt.date_time_format, repr(dtt.tz))

    def test_default_format_call_with_correctly_formatted_date_time(self):
        dtt = dtargs.DateTimeType()
        date_string = '2015-01-02T12:34:56Z'
        assert dtt(date_string) == datetime(2015, 1, 2, 12, 34, 56,
                                            tzinfo=pytz.utc)

    def test_default_format_tz_none_with_correctly_formatted_date_time(self):
        dtt = dtargs.DateTimeType(tz=None)
        date_string = '2015-01-02T12:34:56Z'
        assert dtt(date_string) == datetime(2015, 1, 2, 12, 34, 56)

    def test_default_format_custom_tz_with_correctly_formatted_date_time(
            self):
        est = pytz.timezone('EST')
        dtt = dtargs.DateTimeType(tz=est)
        date_string = '2015-01-02T12:34:56Z'
        assert dtt(date_string) == datetime(2015, 1, 2, 12, 34, 56, tzinfo=est)

    def test_default_format_call_with_incorrectly_formatted_date_time(self):
        date_string = 'Z 12:34:56 02/01/2015'
        with pytest.raises(argparse.ArgumentTypeError):
            dtt = dtargs.DateTimeType()
            dtt(date_string)

    def test_call_with_none(self):
        with pytest.raises(argparse.ArgumentTypeError):
            dtt = dtargs.DateTimeType()
            dtt(None)

    def test_custom_format_call_with_correctly_formatted_date_time(self):
        dtt = dtargs.DateTimeType('%H:%M:%S_%d/%m/%Y')
        date_string = '12:34:56_01/02/2015'
        assert dtt(date_string) == datetime(2015, 2, 1, 12, 34, 56,
                                            tzinfo=pytz.utc)

    def test_custom_format_call_with_incorrectly_formatted_date_time(self):
        date_string = '2015-01-02T12:34:56Z'
        with pytest.raises(argparse.ArgumentTypeError):
            dtt = dtargs.DateTimeType('%H:%M:%S_%d/%m/%Y')
            dtt(date_string)

    def test_custom_format_without_offset_tz_is_none_call_with_valid_date(
            self):
        date_time_format = '%H:%M:%S_%Y-%m-%d'
        date_string = '12:34:56_2015-02-01'
        dtt = dtargs.DateTimeType(date_time_format, tz=None)
        assert dtt(date_string) == datetime(2015, 2, 1, 12, 34, 56,
                                            tzinfo=None)

    def test_custom_format_without_offset_custom_tz_call_with_valid_dt(self):
        est = pytz.timezone('EST')
        dtt = dtargs.DateTimeType('%H:%M:%S_%d/%m/%Y', tz=est)
        date_string = '12:34:56_01/02/2015'
        assert dtt(date_string) == datetime(2015, 2, 1, 12, 34, 56, tzinfo=est)

    @mock.patch('dtargs.datetime')
    def test_custom_format_with_offset_custom_tz_call_with_valid_dt(self,
                                                                    mock_dt):
        date_time_format = 'parsing mocked, format irrelevant'
        date_string = 'parsing mocked, string irrelevant '
        est = pytz.timezone('EST')

        mock_parsed_date_time = datetime(2015, 1, 2, 12, 34, 56,
                                         tzinfo=pytz.utc)
        mock_dt.strptime.return_value = mock_parsed_date_time

        dtt = dtargs.DateTimeType(date_time_format, est)
        assert dtt(date_string) == datetime(2015, 1, 2, 7, 34, 56,
                                            tzinfo=est)
        mock_dt.strptime.assert_called_with(date_string, date_time_format)


    @mock.patch('dtargs.datetime')
    def test_custom_format_with_offset_tz_none_call_with_valid_dt(self,
                                                                  mock_dt):
        date_time_format = 'parsing mocked, format irrelevant'
        date_string = 'parsing mocked, string irrelevant '
        est = pytz.timezone('EST')

        mock_parsed_date_time = datetime(2015, 1, 2, 12, 34, 56, tzinfo=est)
        mock_dt.strptime.return_value = mock_parsed_date_time

        dtt = dtargs.DateTimeType(date_time_format, None)
        assert dtt(date_string) == datetime(2015, 1, 2, 12, 34, 56,
                                            tzinfo=est)
        mock_dt.strptime.assert_called_with(date_string, date_time_format)
