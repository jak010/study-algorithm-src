// 퀵 정렬
// O( N * logN ) -> 평균속도

#include <stdio.h>

int number = 10;

int arr[] = {1, 10, 5,8, 7, 6, 4, 3, 2, 9};

void quickSort(int *data, int start, int end)
{
    // 원소의 개수가 1개 인 경우
    if (start >= end)
    {
        return;
    }

    int key = start;
    int i = start + 1;
    int j = end;
    int temp;
printf("%d\n" ,j);
    while (i <= j)
    {
        while (i <= end && data[i] <= data[key])
        {
            i++;
        }
        while (j > start && data[j] >= data[key])
        {
            j--;
        }
        if (i > j)
        {
            temp = data[j];
            data[j] = data[key];
            data[key] = temp;
        }
        else
        {
            temp = data[j];
            data[j] = data[i];
            data[i] = temp;
        }
    }

    for (int i = 0; i < 10; i++)
    {
        printf("%d ", arr[i]);
    }
    
    printf("\n");
    quickSort(data, start, j - 1);
    quickSort(data, j + 1, end);
    
}

int main(int argc, char const *argv[])
{

    quickSort(arr, 0, number - 1);


    return 0;
}
