#include <stdio.h>

#define INCI(i) {int a=0; ++i;}

int main(void)
{
    int a = 0, b = 0;
    INCI(a);
    INCI(b);
    printf("a is now %d, b is now %d\n", a, b); //a is now 0, b is now 1
    return 0;
}
