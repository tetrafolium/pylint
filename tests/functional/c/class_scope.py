# pylint: disable=R0903,W0232, useless-object-inheritance
"""check for scope problems"""

__revision__ = None


class Well(object):
    """well"""
    attr = 42

    def get_attr(arg=attr):
        return arg * 24

    # +1: [used-before-assignment]
    def get_attr_bad(arg=revattr):
        return revattr * 42

    revattr = 24

    def bad_lambda():
        return get_attr_bad  # [undefined-variable]

    class Data(object):
        """base hidden class"""

    class Sub(Data):
        """whaou, is Data found???"""
        attr = Data()  # [undefined-variable]

    def func(self):
        """check Sub is not defined here"""
        return Sub(), self  # [undefined-variable]
