#include <stdio.h>
#define dprint(expr) printf(#expr" = %g\n", expr)
#define paste(front, back) front ## back
#define swap(t, x, y) t temp = x;\
                      x = y;\
                      y = temp;
int main(void)
{
    int x = 9;
    int y = 3;
    char *name1 = "hello";
    dprint(x/y);
    printf("%s\n", paste(name, 1));
    swap(int, x, y);
    printf("x = %d, y = %d\n", x, y);
    return 0;
}
