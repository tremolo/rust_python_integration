rust_python_integration
=======================

Using Rust to compile a dynamic library to be used in Python with cffi.

This was inspired by an example by Yehuda Katz.
see http://blog.skylight.io/bending-the-curve-writing-safe-fast-native-gems-with-rust

I used cffi for python  to load the library and added a deallocator free_point().
To make sure there are no memory leaks i also added a little test in C to test with valgrind.

Dependencies:

  - Rust Compiler (  I used 0.12.0-nightly )
  - C Compiler  for test and cffi  (gcc or clang)
  - cffi module (  $ pip install cffi )
  - Python
  - valgrind for memory check (optional)

Usage:

Use

$ make 
# to make the library and the test program

$ make lib
# to only make the library

$ make test
# to make the test program

$ make memcheck
# to run the test program with valgrind and check for memory errors

Finally run 
$ python load_libpoint.py 
to use it

----------

Created 2014/10/09 by Lutz Paelike
