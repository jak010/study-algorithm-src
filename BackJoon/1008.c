#include <stdio.h>

int main() {
    double a,b;

    scanf("%lf %lf" ,&a ,&b);
    
    if( b > 10 ) return 0;

    printf("%0.9f" ,a/b);


}