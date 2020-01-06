#include <stdio.h>

int sorted[8];
//  정렬할 갯수의 배열
int number = 8;

void merge(int a[], int m, int middle, int n) {

  int i = m;
  int j = middle + 1;

  int k = m;
  // 작은 순서대로 배열에 삽입
  while (i <= middle && j <= n) {
    if (a[i] <= a[j]) {
      sorted[k] = a[i];
      i++;
    } else {
      sorted[k] = a[j];
      j++;
    }
    k++;
  }

  // 남은 데이터 삽입
  if (i > middle) {
    for (int t = j; t <= n; t++) {
      sorted[k] = a[t];
      k++;
    }

  } else {
    for (int t = i; t <= middle; t++) {
      sorted[k] = a[t];
      k++;
    }
  }
  for (int t = m; t <= n; t++) {
    a[t] = sorted[t];
  }
}

void mergetSort(int a[], int m, int n) {
  if (m < n) {
    int middle = (m + n) / 2;
    mergetSort(a, m, middle);
    mergetSort(a, middle + 1, n);
    merge(a, m, middle, n);
  }
}

int main(int argc, char const *argv[]) {

  int array[8] = {7, 6, 5, 8, 3, 5, 9, 1};
  mergetSort(array, 0, number - 1);
  for (int i = 0; i < number; i++) {
    printf("%d ", array[i]);
  }
  printf("\n");
  return 0;
}
