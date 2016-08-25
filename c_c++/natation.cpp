#include<iostream>
#include<stdlib.h>

using namespace std;

/**
 * polish natation + 3 4=3+4   * + 3 4 5=(3+4)*5
 * reverse polish natation 3 4 +=3+4   3 4 * 5 + = 3*4+5
 */

double natation();

int main() {
  cout << natation();
  return 0;
}

double natation() {
  char str[10];
  cin>>str;
  cout<<"----------" << str <<endl;
  switch (str[0]) {
    case '+':
      return natation() + natation();
    case '-':
      return natation() - natation();
    case '*':
      return natation() * natation();
    case '/':
      return natation() / natation();
    default:
      return atof(str);
  }
}
