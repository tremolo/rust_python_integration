all: lib test

lib:
	rustc points.rs 

test:
	gcc -o test test.c 

memcheck:
	valgrind --tool=memcheck  --leak-check=full  ./test

clean:
	rm  -f libpoints.dylib libpoints.so test
