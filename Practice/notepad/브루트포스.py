""" 브루트 포스,

 브루트 포스로 문제를 풀 떄는 반복문을 사용할 때도 있고, 재귀로 풀때도 있다.

 1. 순열, permutation
 - 순열과 조합은 경우의 수를 구할 떄 유용하게 사용되는 개념이다.
    = n개의 수 중에서 r개를 뽑아 줄을 세우는 총 방법의 수 n! / (n-r)! 이다.
    = python에서는 itertools.permutations를 사용한다.
      = permutation(arr, 4)

2. 조합
- n개의 수 중에서 r 개를 뽑는 가지 수는 n! / (n-r)!r! 이다.
- python에서는 itertools의 combinations을 사용한다.

"""