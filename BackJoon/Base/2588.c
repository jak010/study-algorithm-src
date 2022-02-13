
#include <stdio.h>

int main()
{
    int a = 0;
    int b = 0;

    scanf("%d %d",&a,&b);

    int save_temp = b;

    while( b != 0) {        
        printf("%d\n" , a*(b%10));
        b = b / 10;
    }
        
    printf("%d\n" ,a*save_temp);
    return 0;
}