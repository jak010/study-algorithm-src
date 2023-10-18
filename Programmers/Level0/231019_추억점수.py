name = ["may", "kein", "kain", "radi"]
yearing = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]


def solution(name, yearning, photo):
    hmap = {}
    answer = []
    for name, year in zip(name, yearning):
        if name not in hmap:
            hmap[name] = year
        else:
            pass

    for each in photo:
        temp = 0
        for e in each:
            if score := hmap.get(e):
                temp += score
        answer.append(temp)

    return answer


print(solution(name, yearing, photo))
