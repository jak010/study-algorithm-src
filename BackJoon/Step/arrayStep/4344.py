import sys

# total case
total = int(sys.stdin.readline())

for _ in range(total):
    raw = sys.stdin.readline().split(" ")
    cnt, grade = raw[0], [int(x) for x in raw[1:]]

    avg = sum(grade) / len(grade)

    rate = [x for x in grade if x > avg]

    print("{:.3f}%".format(float(len(rate) / len(grade) * 100)))


# 백준 4344 번 객체 형식으로 바꿔보기
from __future__ import annotations
from typing import Type, List, Optional


class GradeVo:
    def __init__(self, score):
        self.grade_group: List[int] = []

        self.parser(score)

    def parser(self, score: str):
        score = score.split(" ")
        _, grade_group = score[0], [int(x) for x in score[1:]]

        self.grade_group = grade_group


class Grade:
    def __init__(self, index, value):
        self.index = index

        if value < 0 and value > 100:
            raise ValueError("Invalid")
        self.value = value


class Operation:
    def __init__(self, grade_group: List[Grade]):
        self.grade_group: List[Grade] = grade_group

    @property
    def grade_group_size(self):
        return len(self.grade_group)

    @property
    def sum_grade(self):
        return sum([grade.value for grade in self.grade_group])

    @property
    def average(self):
        return self.sum_grade / self.grade_group_size

    @property
    def upper_rate_group(self):
        return [grade.value for grade in self.grade_group
                if grade.value > self.average]

    @property
    def upper_rate_group_length(self):
        return len(self.upper_rate_group)

    @property
    def upper_rate(self):
        return "{:.3f}%".format(float(self.upper_rate_group_length) / self.grade_group_size * 100)


class Processor:
    grade_group: List[Grade] = None

    def __init__(self, count):
        self.count = count

    def set_score(self, grade_group):
        self.grade_group = self._generate_grade(GradeVo(grade_group))

    def process(self):
        for cnt in range(self.count):
            yield cnt

    def _generate_grade(self, grade: GradeVo) -> List[Grade]:
        return [Grade(k, v) for k, v in enumerate(grade.grade_group, start=1)]


if __name__ == '__main__':
    import sys

    total = int(sys.stdin.readline())

    processor = Processor(total)
    for process in processor.process():
        score = sys.stdin.readline()
        processor.set_score(score)
        op = Operation(processor.grade_group)
        print(op.upper_rate)
