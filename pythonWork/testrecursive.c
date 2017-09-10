#include <stdio.h>

void qsort(int *, int, int);

int main(void)
{
    int arr[] = {1, 7, 4, 2, 8, 9, 1};
    qsort(arr, 0, 6);
    int i = 0;
    for(;i <= 6; i++)
        printf("%d\n", arr[i]);
    return 0;
}

void qsort(int *v, int left, int right)
{
    int i, last;
    if(left >= right)
        return;
    int start = left;
    int end = right;
    int key = v[left];

    while(start < end)
    {
        while(start < end && v[end] >= key)
        {
            --end; 
        }
        v[start] = v[end];
        while(start < end && v[start] <= key)
        {
            ++start;
        }
        v[end] = v[start];
    }
    v[start] = key;
    qsort(v, left, start - 1);
    qsort(v, start + 1, right);
}
