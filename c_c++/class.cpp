#include <iostream>
#include <string>

using namespace std;

class Student
{
  private: int height;

  protected: int abc;

  public:
    int a;
    string b;

    void init(int a_, string b_) {
      this->a = a_;
      this->b = b_;
      this->height = 0;
    }

    void print() {
      cout << "name: " << this->b << ", age: " << a << ", height: "<< this->height <<endl;
    }

    void say();
};

void Student::say() {
  cout << this->b <<endl;
}

class Reload
{
  private: int x,y;
  public:
    void init(int x = 0, int y = 0);
    void value(int val) {
      this->x = val;
    }
    void value() {
      this->x = 100;
    }
    void print() {
      cout << "x is " << this->x << ", y is " << this->y <<endl;
    }
};

void Reload::init(int x, int y) {
  this->x = x;
  this->y = y;
}


//contruct function
class Test
{
  private: int x, y;

  public:
    Test(int x=0, int y=0);
    void print() {
      cout << "x is " << this->x << ", y is " << this->y <<endl;
    }
};

Test::Test(int x, int y) {
  this->x = x;
  this->y = y;
}

int main() {
  Student s;
  s.init(24, "sun");
  s.print(); //name: sun, age: 24

  Student *sp = new Student;
  sp->print(); //pointer name: , age: 0, height: 0

  Student *ss = &s;
  cout << ss->a <<endl;

  Student & sss = s;
  cout << sss.b <<endl;

  sss.say();

  Reload r;
  r.init(1);
  r.print(); //x is 1, y is 0
  r.value(20);
  r.print(); //x is 20, y is 0
  r.value();
  r.print(); //x is 100, y is 0

  Test t;
  t.print();   //x is 0, y is 0
  Test t2(1);
  t2.print();  //x is 1, y is 0
  Test *t3 = new Test(2, 3);
  t3->print(); //x is 2, y is 3
}
