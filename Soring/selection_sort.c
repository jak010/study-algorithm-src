// 선택 정렬은 하나씩
// 선택 정렬의 시간 복잡도는 n^2

#include <stdio.h>

int main(int argc, char const *argv[])
{
  int i, j, temp;

  int array[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};

  for (int i = 0; i < 9; i++)
  {
    for (int j = i + 1; j < 10; j++)
    {
      if (array[i] > array[j]) // 오름차순 or 내림차 순
      {
        temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }
    }
  }

  // 정렬된 배열 출력
  for (i = 0; i < 10; i++)
  {
    printf("%d ", array[i]);
  }
  return 0;
}
