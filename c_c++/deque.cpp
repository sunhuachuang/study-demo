#include <iostream>
#include <deque>

using namespace std;

int main() {
  unsigned int i;
  deque<int> d(5);
  cout << d.end() - d.begin() <<endl;

  for (i = 0; i < d.size(); i++)
    d[i] = i;

  d.at(2) = 20;
  d[3] = 30;

  for (i = 0; i < d.size(); i++)
    cout << d[i] <<endl;

  d.pop_back();
  d.push_back(40);
  d.push_front(111);

  for (i = 0; i < d.size(); i++)
    cout << d[i] <<endl;
}
