// 선택 정렬은 하나씩
// 선택 정렬의 시간 복잡도는 n^2

// 선택 정렬은 첫 번째 자료를 두 번쨰 자료부터 마지막 자료까지 차례대로 비교하여
// 최소값을 찾아 첫 번쨰에 놓고 두 번쨰 자료를 세 번쨰 자료부터 마지막 자료까지
// 차례대로 비교하여 그 중 작은 값을 찾아 두 번쨰 위치에 놓는 과정을 반복하며
// 정렬을 수행한다.

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
