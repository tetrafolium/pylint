"""Checks import order rule"""
# pylint: disable=unused-import,ungrouped-imports,wrong-import-order
# pylint: disable=import-error, too-few-public-methods, missing-docstring,using-constant-test, useless-object-inheritance
import astroid  # [wrong-import-position]
import scipy  # [wrong-import-position]
import datetime  # [wrong-import-position]
import os.path

if True:
    from astroid import are_exclusive
try:
    import sys
except ImportError:

    class Myclass(object):
        """docstring"""


if sys.version_info[0] >= 3:
    from collections import OrderedDict
else:

    class OrderedDict(object):
        """Nothing to see here."""
        def some_func(self):
            pass


import six  # [wrong-import-position]

CONSTANT = True

VAR = 0
for i in range(10):
    VAR += i
