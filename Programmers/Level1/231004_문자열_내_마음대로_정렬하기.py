def solution(strings, n):
    answer = strings
    answer.sort(key=lambda x: (x[n], x))

    return answer


strings = ["sun", "bed", "car"]

strings = ["abce", "abcd", "cdx"]

# solution(strings, 1)
print(solution(strings, 2))
