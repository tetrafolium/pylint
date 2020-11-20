# pylint: disable=too-few-public-methods, W0231, print-statement, useless-object-inheritance
# pylint: disable=no-classmethod-decorator
"""Test external access to protected class members."""
from __future__ import print_function


class MyClass(object):
    """Class with protected members."""
    _cls_protected = 5

    def __init__(self, other):
        MyClass._cls_protected = 6
        self._protected = 1
        self.public = other
        self.attr = 0

    def test(self):
        """Docstring."""
        self._protected += self._cls_protected
        print(self.public._haha)  # [protected-access]

    def clsmeth(cls):
        """Docstring."""
        cls._cls_protected += 1
        print(cls._cls_protected)

    clsmeth = classmethod(clsmeth)

    def _private_method(self):
        """Doing nothing."""


class Subclass(MyClass):
    """Subclass with protected members."""
    def __init__(self):
        MyClass._protected = 5
        super(Subclass, self)._private_method()


INST = Subclass()
INST.attr = 1
print(INST.attr)
INST._protected = 2  # [protected-access]
print(INST._protected)  # [protected-access]
INST._cls_protected = 3  # [protected-access]
print(INST._cls_protected)  # [protected-access]


class Issue1031(object):
    """Test for GitHub issue 1031"""
    _attr = 1

    def correct_access(self):
        """Demonstrates correct access"""
        return type(self)._attr

    def incorrect_access(self):
        """Demonstrates incorrect access"""
        if self._attr == 1:
            return type(INST)._protected  # [protected-access]
        return None


class Issue1802(object):
    """Test for GitHub issue 1802"""
    def __init__(self, value):
        self._foo = value
        self.__private = 2 * value

    def __eq__(self, other):
        """Test a correct access as the access to protected member is in a special method"""
        if isinstance(other, self.__class__):
            answer = self._foo == other._foo
            # [protected-access]
            return answer and self.__private == other.__private
        return False

    def not_in_special(self, other):
        """
        Test an incorrect access as the access to protected member is not inside a special method
        """
        if isinstance(other, self.__class__):
            return self._foo == other._foo  # [protected-access]
        return False

    def __le__(self, other):
        """
        Test a correct access as the access to protected member
        is inside a special method even if it is deeply nested
        """
        if 2 > 1:
            if isinstance(other, self.__class__):
                if "answer" == "42":
                    return self._foo == other._foo
        return False

    def __fake_special__(self, other):
        """
        Test an incorrect access as the access
        to protected member is not inside a licit special method
        """
        if isinstance(other, self.__class__):
            return self._foo == other._foo  # [protected-access]
        return False
