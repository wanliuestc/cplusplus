#include <stdio.h>
void swap(void *, int, int);

int main(void)
{
	int arr[] = {1, 2, 3, 4, 5};
	int i = 10;
	void *p = &i;
	void **pp = &p;
	printf("%d\n", *(int *)*pp);
	return 0;
}

void swap(void *arr, int i, int j)
{
}
