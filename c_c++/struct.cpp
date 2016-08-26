#include <iostream>

using namespace std;

struct student {
  char name[10];
  int age;
};

//copy
void reage(student one) {
  one.age = 25;
  cout << "reage: " << one.age <<endl; // 25
}

//pointer
void rearray(int a[]) {
  a[0] = 1;
  cout << "rearray: " << a[0] << ", " << a[1] <<endl; // 1 2
}

//copy
void revariable(int a) {
  a = 2;
  cout << " revariable: " << a << endl; //2
}

/* failure
int return_array() {
  int a[2] = {1, 2};
  return a;
}
*/

//copy
int return_variable() {
  int a = 1;
  return a;
}

//copy
student return_struct() {
  student a = {"sun", 24};
  return a;
}

int main() {
  student sun = {"sun", 24};
  reage(sun); //no change for sun.
  cout << sun.name << ", " << sun.age <<endl; // sun 24

  int a[2] = {2, 2};
  rearray(a);
  cout << "array: " << a[0] << ", " << a[1] <<endl; // 1 2

  int b = 1;
  revariable(b);
  cout << b << endl; //1

  //int c[2] = return_array();
  //cout << "return array: " << c[0] << c[1] <<endl;

  int d = return_variable();
  cout << "return variable: " << d <<endl; // 1

  student e = return_struct();
  cout << "return struct: " << e.name << e.age <<endl; //sun 24

  student f = {"sun", 24};
  student *g = &f;
  cout << (*g).name << g->name <<endl; //sun sun
  return 0;
}
