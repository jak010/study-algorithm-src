// 그리디 알고리즘
// 경우의 수가 존재할 경우, 최선이라고 생각하는 경우르 선택하는 알고리즘


#include <stdio.h>

int main(int argc, char const *argv[])
{
    int money = 1000;
    int array[] = {1,5,10,50,100,500};
    int idx = 0;
    int ans =0;

     
    while( money != 0 ){
       printf("\n [+] current change money : %d", array[idx]);
        int change = money/array[idx];
        
        money -= change * array[idx++];
        ans += change;
        printf("\n [+]money : %d\n [+]ans : %d\n" ,money,ans);
    }

    printf("\n%d",ans);
    return 0;
}
