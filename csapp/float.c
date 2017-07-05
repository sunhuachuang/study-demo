#include <stdio.h>

void bin(unsigned x) {
  if (x > 1)
    bin(x/2);

  printf("%d", x%2);
}

int main() {

  float x = 1.0/5.0;

  bin(1000);

  printf(" 1/5 is %f,  hex is 0x%.8x", x,  x);

  return 0;
}
