#include <stdio.h>

int main(void)
{
    int i = 10;
    int j = 15;
    int *p = &i;
    int *q = &j; 
    //*p = 12;
    *q = *p; 
    return 0;
}
