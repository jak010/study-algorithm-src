"""
Date: 2021.12.20
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
"""
grade = int(input())


def judge(grade):
    if grade >= 90:
        return "A"
    if (grade < 90) and (grade >= 80):
        return "B"
    if (grade < 80) and (grade >= 70):
        return "C"
    if (grade <= 70) and (grade >= 60):
        return "D"

    return "F"


print(judge(grade))
