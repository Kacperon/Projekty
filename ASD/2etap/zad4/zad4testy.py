# zad4testy.py
from testy import *
from zad4test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy

def copyarg( arg ):
    return deepcopy(arg)

def printarg(L, k):
    print(f"k: {k}")
    out = ', '.join([str(x) for x in list2tab(L)])
    print("Wejciowa lista:\t", limit(out))

def printarg(*arg):
    print(f'L={limit(arg[0])}')
    print(f'a={arg[1]}')
    print(f'b={arg[2]}')
    print(f't={arg[3]}')

def printhint( hint ):
    print("Poprawny wynik  : ", hint )

def printsol( sol ):
    print("Otrzymany wynik : ", sol )

def check( hint, sol ):
    return hint==sol        	

def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)

    return TESTS

def runtests( f, all_tests = True ):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

