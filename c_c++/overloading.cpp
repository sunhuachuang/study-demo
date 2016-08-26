#include <iostream>

using namespace std;

int Max(int a, int b, int c) {
  if (a>b && a>c)
    return a;
  else if (b>c && b>a)
    return b;
  else
    return c;
}

int Max(int a, int b) {
  if (a>b)
    return a;
  else
    return b;
}

int main() {
  cout << Max(1, 2) <<endl; //2
  cout << Max(1, 2, 3) <<endl; //3
}
