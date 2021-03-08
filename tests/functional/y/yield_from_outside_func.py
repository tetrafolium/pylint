"""This is gramatically correct, but it's still a SyntaxError"""
yield from [1, 2]  # [yield-outside-function]


def LAMBDA_WITH_YIELD(): return (yield from [1, 2])
