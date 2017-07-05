#include <stdio.h>
#include <math.h>

int uadd_ok(unsigned short x, unsigned short y) {
  unsigned short w = sizeof(x);
  printf("w size is %u, ", w);
  printf("add size is %u, ", sizeof(x+y));

  return x+y-pow(2, w) >= x;
}

int main() {
  unsigned short x = 12345;
  unsigned short y = 12345;

  printf("is ok? %d\n", uadd_ok(x, y));

  unsigned short m = 65535;
  unsigned short n = 12345;

  printf("is ok? %d\n", uadd_ok(m, n));
  return 0;
}
