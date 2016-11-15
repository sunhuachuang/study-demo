#include <iostream>
#include <set>
#include <map>

using namespace std;

/** set & multiset
 * fn: find()
 * fn: insert()
 * fn: count(const T& val)
 * fn: lower_bound(const T& val) -> iterator : [start(), it) 比 val 小的最大位置
 * fn: upper_bound(const T& val) -> iterator : [it, end()) 比val 大的最小位置
 * fn: equal_range(const T& val) -> pair(iterator, iterator) (lower_bound, upper_bound)
 * fn: erase(iterator it) -> iterator后面元素(跟编译器相关)
 */
class A {};
void test_main() {
  multiset<A> a; // == multiset<A less<A>> a,  less: <   greater: >
  //a.insert(A()); //A类没有重载 <  报错
}

int main() {
  string a="aaa", b = "bbb";
  if (a < b) {
    cout << "aaa" <<endl;
  }

  multimap<string, greater<string> > mps;

  multimap<string, double, less<string> > mp;

  mp.insert(make_pair("ok", 2));
}
