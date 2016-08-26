#include <stdio.h>    // c
//#include <iostream> // c++

void print_min(int a, int b) {
  if (a > b)
    printf("%d", a);
  else
    printf("%d", b);
}

int main() {
  void (*pf) (int, int);
  int x = 1, y = 2;
  pf = print_min;
  pf(x, y);
  return 0;
}
