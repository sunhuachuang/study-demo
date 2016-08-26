#include<iostream>

using namespace std;

int main() {
  int a[5] = {1, 2, 3, 4, 5};
  int *pointer = &a[3];

  cout << *pointer <<endl; //4
  *pointer = 44;
  cout << a[3] <<endl; //44

  cout << a <<endl;     // 0x7ffc60759480
  cout << *a <<endl;    // 1
  cout << &a <<endl;    // 0x7ffc60759480
  cout << &a[0] <<endl; // 0x7ffc60759480
  cout << a[0] <<endl;  // 1

  int *p = a;
  cout << p    << endl; //0x7ffc60759480
  cout << *p++ <<endl; // 1
  cout << *p++ <<endl; // 2
  cout << *p <<endl;   // 3

  return 0;
}

void fun() {

  char a[10] = {'1', '2', '3', '4', '5', '6', '7', '8', '9', 0}, *p; //string

  int i = 8;

  p = a + i;

  cout << a <<endl; //123456789
  cout << &a <<endl; //0x7ffeaa088110
  cout << &a[0] <<endl; //123456789
  cout << a[8] <<endl; //9
  cout << &a[8] <<endl; //9
  cout << a+i <<endl; //9
  cout << p <<endl; //9

  cout << p - 3 << endl; //6789
}
