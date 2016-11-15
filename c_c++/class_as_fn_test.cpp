#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>

using namespace std;

int sumSquare(int total, int value) {
  return total + value * value;
}

template <class T>
void PrintInterval(T first, T last) {
  for (; first != last; ++first)
    cout << *first << " ";
}

template <class T>
class SumPowers
{
private:
  int power;

public:
  SumPowers(int p):power(p) {}
  const T operator () (const T& total, const T& value) {
    T v = value;
    for (int i = 0; i < power; i++)
      v = v * value;
    return total + v;
  }
};

//MyMax
template <class T>
class MyMax
{
public:
  const T operator () () {
    T v;
    return v;
  }
};

class MyLess
{
public:
  bool operator () (int a, int b) {
    if (a%10 < b%10)
      return true;
    else
      return false;
  }
};

bool my_less(int a, int b) {
  if (a%10 < b%10)
    return false;
  else
    return true;
}

int main() {
  const int SIZE = 10;
  int a1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  vector<int> v(a1, a1+SIZE);

  cout << "1: ";
  PrintInterval(v.begin(), v.end()); //1: 1 2 3 4 5 6 7 8 9 10
  cout << endl;

  int result = accumulate(v.begin(), v.end(), 0, sumSquare);
  cout << "平方和： " << result << endl; //平方和： 385

  result = accumulate(v.begin(), v.end(), 0, SumPowers<int>(3));
  cout << "3次方和： " << result << endl; //3次方和： 25333


  int b[5] = {91, 82, 34, 56, 19};
  cout << MyMax<int>(b, b+5, MyLess()) <<endl;
  cout << MyMax<int>(b, b+5, my_less()) <<endl;
}
