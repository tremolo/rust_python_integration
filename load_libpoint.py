#!/usr/bin/env python
"""
Small example how to load the shared library created with rust in python
by Lutz Paelike
"""
# pylint: disable=invalid-name

from __future__ import print_function

import sys

import cffi
FFI = cffi.FFI()
FFI.cdef("""
    struct Point{ int x,y; };

    struct Point* make_point(int, int);
    void free_point(struct Point*);

    double get_distance(struct Point*, struct Point*);
    """)

if sys.platform == "darwin":
    LIBNAME = "./libpoints.dylib"
else:
    LIBNAME = "./libpoints.so"

LIB = FFI.dlopen(LIBNAME)

def main():
    """Show use of Rust structs and functions"""
    a = LIB.make_point(20, 20)
    b = LIB.make_point(10, 10)

    print("distance: {:.8g}".format(LIB.get_distance(a, b)))

    LIB.free_point(a)
    LIB.free_point(b)

if __name__ == '__main__':
    main()
