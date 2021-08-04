# pylint: disable=R0903,W0232, useless-object-inheritance
"""check for scope problems"""

__revision__ = None


class Well(object):
    """well"""
    attr = 42

    def get_attr(arg=attr):
        return arg * 24

    # +1: [undefined-variable, used-before-assignment]
    def get_attr_bad(arg=revattr):
        return revattr * 42

    revattr = 24

    def bad_lambda():
        return get_attr_bad  # [undefined-variable]

    bad_gen = list(attr + i for i in range(10))  # [undefined-variable]

    class Data(object):
        """base hidden class"""

    class Sub(Data):
        """whaou, is Data found???"""
        attr = Data()  # [undefined-variable]

    def func(self):
        """check Sub is not defined here"""
        return Sub(), self  # [undefined-variable]


class Right:
    """right"""
    class Result1:
        """result one"""
        OK = 0

    def work(self) -> Result1:
        """good type hint"""
        return self.Result1.OK


class Wrong:
    """wrong"""
    class Result2:
        """result two"""
        OK = 0

    def work(self) -> self.Result2:  # [undefined-variable]
        """bad type hint"""
        return self.Result2.OK
