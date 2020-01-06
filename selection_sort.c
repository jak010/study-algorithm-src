// 선택 정렬은 하나씩

#include <stdio.h>

int main(int argc, char const *argv[]) {
  int i, j, min, index, temp;

  int array[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};

  for (i = 0; i < 10; i++) {
    min = 9999;
    for (j = i; j < 10; j++) {
      if (min > array[j]) {
        min = array[j]; // min 보다 작은 원소값이 있을 경우 배열 원소를 min으로
                        // 대체
        index = j; // j 는 배열의 인덱스
      }
    }
    temp = array[i];
    array[i] = array[index];
    array[index] = temp;
  }

  for (i = 0; i < 10; i++) {
    printf("%d ", array[i]);
  }
  printf("\n");

  return 0;
}
