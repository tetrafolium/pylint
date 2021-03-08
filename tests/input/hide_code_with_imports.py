import p
import o
import n
import m
import l
import k
import j
import i
import h
import g
import f
import e
import d
import c
import b
import a
def quicksort(a): return qs1(a, 0, len(a)-1)


def qs1(a, lo, hi): return qs2(a, lo, hi) if lo < hi else a
def qs2(a, lo, hi): return qs3(lo, hi, *qsp(a, lo, hi))


def qs3(lo, hi, a, p): return qs1(qs1(a, p+1, hi), lo, p-1)
def qsp(a, lo, hi): return qsp1(a, lo, hi, a[hi], lo, lo)


def qsp1(a, lo, hi, p, i, j): return qsp2(a, lo, hi, p, i, j, j < hi)
def qsp2(a, lo, hi, p, i, j, c): return qspt(
    a, lo, hi, p, i, j, qsp3 if c else qsp7)


def qspt(a, lo, hi, p, i, j, n): return n(a, lo, hi, p, i, j)


def qsp3(a, lo, hi, p, i, j): return qsp4(a, lo, hi, p, i, j, a[j] < p)
def qsp4(a, lo, hi, p, i, j, c): return qspt(
    a, lo, hi, p, i, j, qsp5 if c else qsp6)


def qsp5(a, lo, hi, p, i, j): return qsp1(sw(a, i, j), lo, hi, p, i+1, j+1)
def qsp6(a, lo, hi, p, i, j): return qsp1(a, lo, hi, p, i, j+1)
def qsp7(a, lo, hi, p, i, j): return (sw(a, i, hi), i)
def sw(a, i, j): return sw1(enumerate(a), i, j, a[i], (-1, a[j]))
def sw1(a, i, j, ai, aj): return sw2(
    [aj if x[0] == i else x for x in a], j, ai)


def sw2(a, j, ai): return [ai if x[0] == j else x[1] for x in a]
