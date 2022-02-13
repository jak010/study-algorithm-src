/*
  문제
  두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.
  첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
*/

#include <stdio.h>

int main() {
    double a,b;

    scanf("%lf %lf" ,&a ,&b);
    
    if( b > 10 ) return 0;

    printf("%0.9f" ,a/b);


}