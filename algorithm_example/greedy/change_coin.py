def make_change(conins: list, amount):
    conins.sort(reverse=True)
    change = []

    for coin in conins:
        while amount >= coin:
            change.append(coin)
            amount -= coin

    if amount == 0:
        return change
    else:
        return None


conin_set = [1, 5, 10, 25]

amount_to_make = 63  # 거슬러 줘야 할 금액

change_result = make_change(conin_set, amount_to_make)
if change_result:
    print(change_result)
