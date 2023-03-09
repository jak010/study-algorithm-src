def slope(p2, p1):
    x2_x1 = p2[0] - p1[0]
    y2_y1 = p2[1] - p1[1]

    return y2_y1 / x2_x1


def solution(dots):
    p1 = dots[0:2]
    p2 = dots[2:]

    x1, x2 = p1[0][0], p1[1][0]
    y1, y2 = p1[0][1], p1[1][1]

    x3, x4 = p2[0][0], p2[1][0]
    y3, y4 = p2[0][1], p2[1][1]

    p1 = (x1, y1)
    p2 = (x2, y2)

    p3 = (x3, y3)
    p4 = (x4, y4)

    # 평행인 조건, 기울기는 같고 y절편은 다르다.
    if slope(p2, p1) == slope(p4, p3):
        return 1
    if slope(p4, p2) == slope(p3, p1):
        return 1
    if slope(p4, p1) == slope(p3, p2):
        return 1

    return 0


if __name__ == '__main__':
    coordiante = [[1, 4], [9, 2], [3, 8], [11, 6]]
    coordiante2 = [[3, 5], [4, 1], [2, 4], [5, 10]]
    coordiante3 = [[1, 2], [3, 4], [1, 2], [3, 4]]

    s = solution(coordiante3)
    print(s)
