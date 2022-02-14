import sys

total = int(sys.stdin.readline())

subject_grade = [int(x) for x in sys.stdin.readline().split(' ')]
MAX_SUBJECT_GRADE = max(subject_grade)
calcurator = [grade / MAX_SUBJECT_GRADE * 100
              for grade in subject_grade]

print(sum(calcurator) / total)
