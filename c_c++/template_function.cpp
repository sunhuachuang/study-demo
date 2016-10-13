#include <iostream>

using namespace std;

template <typename T>
inline const T& maxnum(const T& x, const T& y) {
  if (y > x)
    return y;
  else
    return x;
}

int main() {
  int a = 1, b = 2;
  double c = 2.0, d = 3.0;
  double e = 2.1, f = 3.1;
  char g = 'a', h = 'b';

  cout << maxnum(a, b) <<endl; //2
  cout << maxnum<int>(a, b) <<endl; //2
  cout << maxnum(c, d) <<endl; //3
  cout << maxnum<double>(e, f) <<endl; //3.1
  cout << maxnum(g, h) <<endl; //b
}
