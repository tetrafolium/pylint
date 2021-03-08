"""This is gramatically correct, but it's still a SyntaxError"""
yield 1  # [yield-outside-function]


def LAMBDA_WITH_YIELD(): return (yield)
