// 서로 인접한 두 원소를 검사하여 정렬하는 알고리즘
// n 과 n+1 비교함
// 선택 정렬과 유사하지만 헷갈리면 안됨


// BEST : n^2
// AVG  : n^2
// Worst : n^2
#include <stdio.h>

int main(int argc, char const *argv[]) {
  int i, j, temp;

  int array[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};

  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 9; j++) {

      if (array[j] > array[j + 1]) {
        temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }

  for (i = 0; i < 10; i++) {
    printf("%d ", array[i]);
  }
  printf("\n");

  return 0;
}
