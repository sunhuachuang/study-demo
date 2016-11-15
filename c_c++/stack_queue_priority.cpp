#include <iostream>
#include <stack>
#include <queue>

using namespace std;

/**
 * fn: push() 添加
 * fn: pop() 删除
 * fn: top() 栈顶或者队头
 */

int main() {
  priority_queue<double> priorities;

  priorities.push(1.1);
  priorities.push(2);
  priorities.push(5);
  priorities.push(42);
  priorities.push(0);

  while (!priorities.empty()) {
    cout << priorities.top() << " ";
    priorities.pop();
  }
  cout << "----------" << endl;

  stack<int> q;
  q.push(1);
  q.push(2);
  q.push(3);
  while (!q.empty()) {
    cout << q.top() << " ";
    q.pop();
  }
  cout << "----------" << endl;
}
