# -*- coding: utf-8 -*-

from datetime import date
import argparse
import dtargs
import pytest


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
