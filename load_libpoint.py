"""
Small example how to load the shared library created with rust in python
by Lutz Paelike 
"""

import sys

import cffi
ffi=cffi.FFI()

ffi.cdef ("""
    struct Point { int x,y; }; 
    
    struct Point* make_point(int, int);
    void free_point(struct  Point*);

    double get_distance( struct  Point*, struct  Point*);
    """)

if sys.platform == "darwin":
    libname = "libpoints.dylib"
else:
    libname = "libpoints.so"

lib = ffi.dlopen(libname)


a = lib.make_point(20,20)
b = lib.make_point(10,10)

print "distance : ",lib.get_distance(a,b)

lib.free_point(a)
lib.free_point(b)

