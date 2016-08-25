#include <iostream>
#include "max.h"

using namespace std;

int a, b;

void exchange(int a, int b) {
  int p;
  p = a;
  a = b;
  b = p;
}

void exchange2() {
  int p;
  p = a;
  a = b;
  b = p;
}

void change_array(int a[]) {
  a[0] = 20;
  a[1] = 30;
}

int main() {
  cin >> a >> b;
  exchange(a, b);
  cout << a << " " << b <<endl;
  exchange2();
  cout << a << " " << b <<endl;

  int c[2] = {1, 2};
  cout << "pre-array: " << c[0] << " " << c[1] <<endl;
  change_array(c);
  cout << "array: " << c[0] << " " << c[1] <<endl;

  return 0;
}
