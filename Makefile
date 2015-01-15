.PHONY: all lib test memcheck clean

OS := $(shell uname)

ifeq ($(OS),Darwin)
    LIB = libpoints.dylib
else
    LIB = libpoints.so
endif

all: $(LIB) test

lib: $(LIB)

$(LIB): points.rs
	rustc points.rs

ctest: test.c $(LIB)
	gcc -o ctest test.c -g -ldl

test: $(LIB) ctest
	./ctest
	python load_libpoint.py

memcheck: ctest
	valgrind --tool=memcheck --leak-check=full ./ctest

clean:
	rm -f $(LIB) ctest
