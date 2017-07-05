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

  int a = -2147483647-1 == 2147483648U;

  unsigned int b = -2147483647-1;
  unsigned int c = -2147483647;

  printf("a is %d b is %u c is %u\n", a, b, c);

  unsigned aa[4] = {
    0x00000076,
    0x87654321,
    0x000000C9,
    0xEDCBA987
  };

  for (int i = 0; i < 4; i++) {
    printf("func1 is 0x%.8x\t", func1(aa[i]));
    printf("func2 is 0x%.8x\n", func2(aa[i]));
  }

  return 0;
}

int func1(unsigned word) {
  return (int) ((word << 24) >> 24);
}

int func2(unsigned word) {
  return ((int) word << 24) >> 24;
}
