#include "static.h"
#include <stdio.h>

int main(void)
{
    printf("a = %d\n", a); 
    test();
    char arr[] = { 'a', 'b', 'c', 0};
    return 0;
}

static int test(void)
{
    static int b = 10;
    b++;
    printf("b = %d\n", b);
    return 0;
}
