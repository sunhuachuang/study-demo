#include <iostream>

using namespace std;

//函数对象 重载了 () 的类就是函数对象
class MyAverage
{
public:
  double operator () (int a1, int a2, int a3) {
    return (double) (a1+a2+a3)/3;
  }
};

int main() {
  MyAverage my;
  cout << my(1, 2, 3) <<endl;
  cout << my.operator()(1, 2, 3) <<endl;
}
