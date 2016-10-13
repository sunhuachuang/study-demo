#include <iostream>
#include <vector>

using namespace std;

int main() {
  unsigned int i;
  int a[5] = {1, 2, 3, 4, 5};

  // v
  // v(5) 五个元素,
  // v(5, const T &val) v(5, 1) 五个初始化1,
  // v(iterator frist, iterator last) [first, last) 拷贝另一个可迭代对象的一部分
  // fn: pop_back() delete last
  // fn: push_back(const T& val) add to last
  // fn: int size() number in vector
  // fn: T& front() 第一个元素的引用
  // fn: T& back() 最后一个元素的引用
  vector<int> v(5);
  cout << v.end() - v.begin() <<endl;

  for (i = 0; i < v.size(); i++)
    v[i] = i;

  v.at(2) = 20;
  v[3] = 30;
  v.pop_back();
  v.push_back(40);

  for (i = 0; i < v.size(); i++)
    cout << v[i] <<endl;

  cout << "all: " << v.capacity() <<endl; //5
  cout << "max size: " << v.max_size() <<endl; //max size: 4611686018427387903

  cout << "-----------" <<endl;

  vector<int> v2(a, a+5);
  v2.insert(v2.begin() + 2, 3333);
  vector<int>::iterator j;
  for (j = v2.begin(); j < v2.end(); j++)
    cout << &j << ": " << *j <<endl;

  cout << "all: " << v2.capacity() <<endl; //all: 10
  cout << "max size: " << v2.max_size() <<endl; //max size: 4611686018427387903
}
