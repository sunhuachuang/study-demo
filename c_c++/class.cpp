#include <iostream>
#include <string>

using namespace std;

class Student {
  public:
    int a;
    string b;

  void init(int a_, string b_) {
    this->a = a_;
    this->b = b_;
  }

  void print() {
    cout << "name: " << this->b << ", age: " << a <<endl;
  }

  void say();
};

void Student::say() {
  cout << this->b <<endl;
}

int main() {
  Student s;
  s.init(24, "sun");
  s.print(); //name: sun, age: 24

  Student *ss = &s;
  cout << ss->a <<endl;

  Student & sss = s;
  cout << sss.b <<endl;

  sss.say();
}
