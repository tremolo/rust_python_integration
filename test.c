#include <dlfcn.h>
#include <stdio.h>

#ifdef __APPLE__
#define LIBEXT "dylib"
#else
#define LIBEXT "so"
#endif

typedef struct Point* (_make_point)(int x, int y);
typedef struct Point* (_free_point)(struct Point* p);

typedef double (_get_distance)(struct Point* a, struct Point* b);

int main(int argc, char *argv[]) {
    void *myso = dlopen("./libpoints." LIBEXT, RTLD_NOW);

    _make_point *make_point = dlsym(myso, "make_point");
    _free_point *free_point = dlsym(myso, "free_point");

    _get_distance *get_distance = dlsym(myso, "get_distance");

    struct Point*  a = make_point(10,10);
    struct Point*  b = make_point(20,20);

    double d = get_distance(a,b);
    printf("distance: %f\n", d);

    free_point(a);
    free_point(b);

    dlclose(myso);

    return 0;
}
