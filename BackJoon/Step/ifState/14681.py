"""
Date: 2021.12.20
예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.

점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.
"""

x = int(input())
y = int(input())


def judged(x, y):
    if int(x) > 0 and int(y) > 0:
        return 1
    elif int(x) < 0 and int(y) > 0:
        return 2
    elif int(x) < 0 and int(y) < 0:
        return 3
    elif int(x) > 0 and int(y) < 0:
        return 4


print(judged(x, y))

import unittest


class QuadrantTest(unittest.TestCase):

    def test_quadrant_first(self):
        x = 10
        y = 5
        self.assertEqual(judged(x, y), 1)

    def test_quadrant_two(self):
        x = -10
        y = 5
        self.assertEqual(judged(x, y), 2)

    def test_quadrant_three(self):
        x = -10
        y = -5
        self.assertEqual(judged(x, y), 3)

    def test_quadrant_four(self):
        x = 10
        y = -5
        self.assertEqual(judged(x, y), 4)


if __name__ == '__main__':
    unittest.main()
