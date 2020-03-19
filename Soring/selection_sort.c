// 선택 정렬은 하나씩
// 선택 정렬의 시간 복잡도는 n^2

// 선택 정렬은 첫 번째 자료를 두 번쨰 자료부터 마지막 자료까지 차례대로 비교하여
// 최소값을 찾아 첫 번쨰에 놓고 두 번쨰 자료를 세 번쨰 자료부터 마지막 자료까지
// 차례대로 비교하여 그 중 작은 값을 찾아 두 번쨰 위치에 놓는 과정을 반복하며
// 정렬을 수행한다.

// BEST : n^2
// AVG  : n^2
// Worst : n^2

#include <stdio.h>

int main(int argc, char const *argv[])
{
  int i, j, temp;

  int array[10] = {1, 5, 8, 7, 10, 6, 4, 3, 2, 9};
  int cur_min;
  
  // Selection Sortring
  for (int i = 0; i <= 9; i++)
  {
    for (int j = i + 1; j <= 10; j++)
    {
      // Setup Minimum Value;
      cur_min = array[i];
     
      // 현재 최소값보다 작은 값이 있을 때 바꿔줌
      if (cur_min > array[j])
      {
        temp = array[j]; 
        array[j] = array[i];
        array[i] = temp;
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
