#include <iostream>

using namespace std;

//change a b
void swap(int &a, int &b) {
  int tmp = a;
  a = b;
  b = tmp;
}

int g = 1;

int &return_g() {
  return g;
}

int main() {
  int n = 10;
  int &r = n;
  cout << r <<endl; //10
  r = 20;
  cout << n <<endl; //20
  cout << r <<endl; //20

  int a = 1, b = 2;
  int &c = a;
  cout << c << endl; //1
  c = b; // like a = b;
  cout << c <<endl; //2
  cout << a <<endl; //2

  int n1 = 1,  n2 = 2;
  swap(n1, n2);
  cout << "n1: " << n1 << ", n2: " << n2 <<endl; //n1: 2, n2: 1

  cout << "g1: " << g <<endl; //g1: 1
  return_g() = 2;
  cout << "g2: " << g <<endl; //g2: 2

  int t = 'a';
  cout << t << endl;

  return 0;
}
