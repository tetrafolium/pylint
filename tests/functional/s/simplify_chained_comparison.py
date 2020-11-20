"""Test that some boolean expression statement tests can be simplified."""

# pylint: disable=missing-docstring, invalid-name, no-else-return, too-many-branches


def test_simplify_chained_comparison_1():
    a = 1
    b = 2
    c = 3
    return a < b and b < c  # [chained-comparison]


def test_simplify_chained_comparison_2():
    a = 1
    return a < 10 and a > 1  # [chained-comparison]


def test_simplify_chained_comparison_3():
    a = 1
    b = 2
    c = 3
    d = 4
    if a < 10 and a > 1:  # [chained-comparison]
        pass
    elif a > 1 and a < 10:  # [chained-comparison]
        pass
    elif a > 1 and a <= 10:  # [chained-comparison]
        pass
    elif a > 1 and a < 10 and b == 2:  # [chained-comparison]
        pass
    elif a > 1 and c == b and a < 10:  # [chained-comparison]
        pass
    elif a > 100 and c == b and a < 10:  # [chained-comparison]
        # In this comparison we are not checking whether left bound is actually
        # lower than right bound or not.
        pass
    elif a < b and b < c:  # [chained-comparison]
        pass
    elif a > b and b > c:  # [chained-comparison]
        pass
    elif a < b and a == 1 and b < c:  # [chained-comparison]
        pass
    elif a < b and b < c and c == 786:  # [chained-comparison]
        pass
    elif a < b and b < 0 and c == 786:  # [chained-comparison]
        pass
    elif a < b and c == 786 and b < 0:  # [chained-comparison]
        pass
    elif c == 786 and b < 0 and a < b:  # [chained-comparison]
        pass
    elif a < b < c and c < d:  # [chained-comparison]
        pass
    elif b < c < d and a < b:  # [chained-comparison]
        pass
    elif a < b < c and a < b and b < c:  # [chained-comparison]
        pass


def test_not_simplify_chained_comparison_1():
    a = 1
    b = 2
    c = 3
    d = 4
    if a < 10 and b > 1:
        pass
    elif a > 1 and b < 10:
        pass
    elif a > 1 and a == 10:
        pass
    elif a == 1 and b == 2:
        pass
    elif a > 1 and a > 10:
        pass
    elif a < 100 and a < 10:
        pass
    elif a < b and a < c:
        pass
    elif a < b and a == 1 and a < c:
        pass
    elif a < b and a < c and c == 786:
        pass
    elif a < b < c and b < d:
        pass
    elif a < b < c and a < d:
        pass
    elif b < c < d and a < c:
        pass
    elif b < c < d and a < d:
        pass
