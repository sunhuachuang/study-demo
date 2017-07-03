#include <stdio.h>

int main() {
  int x[] = {1, 2};
  int y[] = {3, 4};

  *y = *x ^ *y; //数组指针指向第一个元素
  *x = *x ^ *y;
  *y = *x ^ *y;

  for (int i = 0; i < 2; i++ ) {
    printf("x[%d] = %d\n", i, x[i]); // [3, 2]
  }

  for (int i = 0; i < 2; i++ ) {
    printf("y[%d] = %d\n", i, y[i]); // [1, 4]
  }

  int a = 1;
  int b = 2;
  int *ap;
  int *bp;

  ap = &a;
  bp = &b;

  *bp = *ap ^ *bp;
  *ap = *ap ^ *bp;
  *bp = *ap ^ *bp;

  printf("a is %d, b is %d\n", a, b); // a is 2, b is 1

  return 0;
}
