def solution(order):
    total = 0

    for x in order:

        if x.find("americano") != -1:
            total += 4500
        if x.find('cafelatte') != -1:
            total += 5000
        if x.find('anything') != -1:
            total += 4500

    return total


if __name__ == '__main__':
    print(solution(order=["cafelatte", "americanoice", "hotcafelatte", "anything"]))
