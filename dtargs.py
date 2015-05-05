# -*- coding: utf-8 -*-

import argparse
from datetime import datetime


class DateType(object):
    """Factory for creating datetime.date object types

    Instances of DateType are typically passed as type= arguments to the
    ArgumentParser add_argument() method.

    :param date_format: A date format string that datetime.strptime accepts
                        (default '%Y-%m-%d')
    :type date_format: str
    """

    def __init__(self, date_format='%Y-%m-%d'):
        self.date_format = date_format

    def __call__(self, string):
        try:
            return datetime.strptime(string, self.date_format).date()
        except (TypeError, ValueError) as e:
            raise argparse.ArgumentTypeError('could not parse "%s" as "%s"'
                                             % (string, self.date_format))

    def __repr__(self):
        return '%s(date_format="%s")' % (type(self).__name__, self.date_format)
