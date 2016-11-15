#include<iostream>

using namespace std;

void change(int *p1, int *p2) {
  int x = 0;
  x = *p1;
  *p1 = *p2;
  *p2 = x;
}

//read-only location
void change2(const int *p1, const int *p2) {
  cout << &p1 <<endl;
  cout << &p2 <<endl;
}

int sum(int *s, int n) {
  int sum = 0;
  for (int i = 0; i < n; i++, s++) {
    sum += *s;
  }
  return sum;
}

//会释放掉
int *test() {
  //int value = 1;
  //return &value;
}

void test2() {
  int a = 0;
  static int b = 0;
  a += 1;
  b += 1;
  cout << "a is: " << a << endl; // 1 1 1 1 1
  cout << "b is: " << b << endl; // 1 2 3 4 5
}

int main() {
  int a, b, *p1, *p2;
  cin>>a>>b;

  p1 = &a;
  p2 = &b;
  const int *p3 = &a; //only read

  change(p1, p2);
  //change2(p1, p2);
  cout << "a is: " << a << ", b is: " << b <<endl;

  int c[] = {1, 2, 3, 4, 5};

  cout << sum(c, 5) << endl;

  for (int i=0; i<5; i++) {
    test2();
  }

  return 0;
}
