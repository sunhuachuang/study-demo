#include <iostream>

using namespace std;

int add(int a, int b, int c=3, int d=4) {
  return a + b + c + d;
}

int main() {
  cout << add(1, 2) <<endl; //10
  cout << add(1, 2, 4) <<endl; //11
  return 0;
}
