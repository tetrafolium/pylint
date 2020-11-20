# pylint: disable=missing-docstring, too-few-public-methods, useless-object-inheritance

class Aaaa(object):
    pass


class Bbbb(object):
    pass


class Cccc(object):
    pass


class Dddd(object):
    pass


class Eeee(object):
    pass


class Ffff(object):
    pass


class Gggg(object):
    pass


class Hhhh(object):
    pass


# [too-many-ancestors]
class Iiii(Aaaa, Bbbb, Cccc, Dddd, Eeee, Ffff, Gggg, Hhhh):
    pass


class Jjjj(Iiii):  # [too-many-ancestors]
    pass
