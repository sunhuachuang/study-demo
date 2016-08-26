#include<iostream>

using namespace std;

int main() {
  int c = 10;

  cout << c <<endl; //10
  cout << &c <<endl; //0x7ffdb231384c
  cout << sizeof(&c) <<endl; //8
  cout << *&c <<endl; //10

  int *pointer = NULL; //pointer variable

  pointer = &c;
  cout << pointer <<endl; //0x7ffdb231384c
  cout << *pointer <<endl; //10

  pointer++;
  cout << pointer <<endl; //0x7ffdb2313850

  return 0;
}
