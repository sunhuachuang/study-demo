#include <iostream>
#include <list>

using namespace std;

/**
 * fn: push_front()          add to front
 * fn: pop_front()           delete the front
 * fn: sort()                sort (STL sort not suitable to list)
 * fn: remove(const T& val)  delete val = val element
 * fn: unique()              unique the list like set()
 * fn: merge(otherlist)      empty all element in otherlist and merge to list
 * fn: reverse()             reverse list
 * fn: splice(p, otherlist, p1, p2) insert some element in otherlist into this list some element front, and remove the elements from otherlist
 */
class A
{
private:
  int n;
public:
  A(int n_) {
    n = n_;
  }

  //友元重载 friend function
  friend bool operator <(const A& a1, const A& a2);
  friend bool operator ==(const A& a1, const A& a2);
  friend ostream& operator <<(ostream& o, const A& a);
};

bool operator <(const A& a1, const A& a2) {
  return a1.n < a2.n;
}

bool operator ==(const A& a1, const A& a2) {
  return a1.n == a2.n;
}

//cout <<
ostream& operator <<(ostream& o, const A& a) {
  o << a.n;
  return o;
}

template <class T>
void PrintList(const list<T>& l) {
  int tmp = l.size();
  if (tmp > 0) {
    typename list<T>::const_iterator i;
    for (i = l.begin(); i != l.end(); i++) {
      cout << *i << ", ";
    }
  }
}

int main() {
  list<A> l1, l2;
  l1.push_back(1);
  l1.push_back(2);
  l1.push_front(3);

  l2.push_back(10);
  l2.push_back(20);
  l2.push_front(30);

  cout << "list1: ";
  PrintList(l1);// 3, 1, 2,
  cout << endl;

  cout << "list2: ";
  PrintList(l2); //30, 10, 20,
  cout << endl;

  l2.sort();
  cout << "list2s: ";
  PrintList(l2); //10, 20, 30,
  cout << endl;

  A a1 = A(1);
  A a2 = A(2);
  if (a1 < a2)
    cout << "a1 < a2" << endl; //
  else
    cout << "a1 >= a2" << endl;
}
