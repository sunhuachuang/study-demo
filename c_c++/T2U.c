#include <stdio.h>

// T2U(x) 共w位 if x >=0  => x
//              if x < 0  => 2 ** w + x
int main() {
  short int v = -12345;
  unsigned short int uv = (unsigned short) v;

  printf("v is %d, uv is %u\n", v, uv);

  short vv = -8;
  unsigned short uvv = (unsigned short) vv;
  printf("v is %d, uv is %u\n", vv, uvv);

  return 0;
}
