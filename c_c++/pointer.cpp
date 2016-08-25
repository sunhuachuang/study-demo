#include<iostream>

using namespace std;

int main() {
  int c = 10;

  cout << c <<endl; //10
  cout << &c <<endl; //0x7ffc63a62114
  cout << sizeof(&c) <<endl; //8
  cout << *&c <<endl; //10

  return 0;
}
