a = [2, 5, 1, 9, 7]
print(sorted(a))

# sorted는 숫자가 아니라 문자도 정렬이 가능함
b = 'zbfseqa'
print(sorted(b))

# join과 함께 이용하면 리스트로 반환 가능
b = 'zbdaf'
print(''.join(sorted(b)))

# list의 sort메소드
# 제자리 정렬(in-place Sort)임 입력을 출력으로 덮어씌움

# list의 sort 메소드는 반환값이 없으므로 주의가 필요
a_sort = a.sort()
print(a_sort)

# 어떻게?
a.sort()  # <- 이렇게 써야됨
print(a)

# sorted 메소드를 key 인자를 통해 정렬 기준을 정할 수 있음
c = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(c, key=len))

print("=" * 10)
a = ['cde', 'cfc', 'abc']


def fn(s):
    print(s)
    return s[0], s[-1]


print(sorted(a, key=fn))
print(sorted(a))
