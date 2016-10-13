#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {
  //int array[10] = {10, 20, 30, 40};
  vector<int> v;

  v.push_back(1);
  v.push_back(2);
  v.push_back(3);
  v.push_back(4);

  vector<int>::iterator p;
  p = find(v.begin(), v.end(), 3);
  if (p != v.end())
    cout << *p <<endl; //3
  cout << &p <<endl; //0x7ffec6021bf0
}
