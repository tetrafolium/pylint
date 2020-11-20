# pylint: disable=undefined-variable
"""test suspicious lambda expressions
"""

__revision__ = ''

# Some simple examples of the most commonly encountered forms.
# +1: [unnecessary-lambda]


def _(): return list()  # replaceable with "list"
# +1: [unnecessary-lambda]
def _(x): return hash(x)  # replaceable with "hash"
# +1: [unnecessary-lambda]
def _(x, y): return min(x, y)  # replaceable with "min"


# A function that can take any arguments given to it.
_ANYARGS = lambda *args, **kwargs: 'completely arbitrary return value'

# Some more complex forms of unnecessary lambda expressions.
# +1: [unnecessary-lambda]
_ = lambda *args: _ANYARGS(*args)
# +1: [unnecessary-lambda]
_ = lambda **kwargs: _ANYARGS(**kwargs)
# +1: [unnecessary-lambda]
_ = lambda *args, **kwargs: _ANYARGS(*args, **kwargs)
# +1: [unnecessary-lambda]
_ = lambda x, y, z, *args, **kwargs: _ANYARGS(x, y, z, *args, **kwargs)

# Lambdas that are *not* unnecessary and should *not* trigger warnings.


def _(x): return x
def _(x): return x()
def _(x=4): return hash(x)
def _(x, y): return list(range(y, x))
def _(x): return list(range(5, x))
def _(x, y): return list(range(x, 5))
def _(x, y, z): return x.y(z)
def _(): return 5


_ = lambda **kwargs: _ANYARGS()
_ = lambda **kwargs: _ANYARGS(**dict([('three', 3)]))
_ = lambda **kwargs: _ANYARGS(**{'three': 3})
_ = lambda dict_arg, **kwargs: _ANYARGS(kwargs, **dict_arg)
_ = lambda *args: _ANYARGS()
_ = lambda *args: _ANYARGS(*list([3, 4]))
_ = lambda *args: _ANYARGS(*[3, 4])
_ = lambda list_arg, *args: _ANYARGS(args, *list_arg)
def _(): return _ANYARGS(*[3])
def _(): return _ANYARGS(**{'three': 3})
def _(): return _ANYARGS(*[3], **{'three': 3})
def _(): return _ANYARGS(func=42)

# Don't warn about this.


def _(): return code().analysis()


_ = lambda **kwargs: dict(bar=42, **kwargs)
