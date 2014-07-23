#include <stdio.h>

typedef struct Vector {
	int x;
	int y;
} Vector;

int l = 1;

int f() {
	return 1;
}

int main(int argc, char const* argv[])
{
	int a = 0;
	int b = 2;
	char c = 'a';
	Vector v = {1, 2};
	int arr[3] = {3, 4, 5};
	printf("hello%d%d%c\n",a ,b ,c);
	printf("x:%d, y:%d\n", v.x, v.y);
	printf("%d\n",f());
	for(; a < 3; ) {
		printf("%d\n", f());
	}
	return 0;
}
