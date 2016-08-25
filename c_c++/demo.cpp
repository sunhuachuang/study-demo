#include <iostream>
#include "max.h"

using namespace std;

//above the main can use like: float max(float, float); 原型
int absolute(int n) {
  if (n < 0)
    return -n;
  else
    return n;
}

void show() {
  cout << "*****show*********"<<endl;
  cout << "*****somethings*********"<<endl;
}

int main() {      //void main() old use.
  int a = 0;
  show();
  cout <<"max number 1 & 2:" << max(1, 2) <<endl;
  cout << "input number: ";
  cin>>a;
  cout << a <<endl;
  // cout << sqrt(100) <<endl;
  // cout << pow(2, 3) <<endl;
  // cout << strlen("str1") <<endl;
  // cout << strcmp("str1", "str2");
  // cout << atoi("100") <<endl;
  int result;
  result = absolute(-10);
  cout << result <<endl;
  return 0;
}
