#include <iostream>

using namespace std;

inline int add_one(int a) {
  return a+1;
}

int main() {
  int a = 10;
  cout << add_one(a) << endl; //11
  cout << a <<endl; //10
}
