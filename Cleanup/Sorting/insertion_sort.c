// 시간복잡도는 선택,버블 정렬과 같음
// 연산의 횟수는 더 적음, 선택,버블 정렬보다는 효율적

// 특정 원소를 기준으로 앞의 원소는 정렬되어 있다 가정함

#include <stdio.h>
#define MAX_SIZE 5

int main()
{
    int array[] = {4, 3, 2, 1, 5};
    int i, j, temp;

    for (int i = 0; i < 5; i++)
    {
        j = i;
        while (array[j] > array[j + 1])
        {
            temp = array[j];
            array[j] = array[j+1];
            array[j+1] = temp;
            j--;
        }
    }

    for (int i = 0; i < 5; i++)
    {
        printf("%d", array[i]);
    }
    return 0;
}