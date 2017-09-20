#include <stdio.h>

int main(void)
{
	int a[] = {1, 3, 5, 7};
	int b[] = {2, 4, 6, 9};
	int i, j;
	for(i = 0; i < 4; i++)
	{
		for(j = 0; j < 4; j++)
		{
			if (a[i] == b[j])
				goto found;
		}
	}
	printf("not found\n");
	goto end;
found:
	printf("found\n");
end:	return 0;
}
