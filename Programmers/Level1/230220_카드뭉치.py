def solution(cards1, cards2, goal):
    while goal:

        if cards1 and cards1[0] == goal[0]:
            cards1.pop(0)
        elif cards2 and cards2[0] == goal[0]:
            cards2.pop(0)
        else:
            return "No"
        goal.pop(0)
    return "Yes"


cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

print(solution(cards1, cards2, goal))
