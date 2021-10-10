def lcp(strs):
    if not strs:
        return ""

    shortest = min(strs, key=len)

    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    return shortest


def lcp2(strs):
    letter_groups, longest_pre = zip(*strs), ""

    print(letter_groups, longest_pre)

    for letter_group in letter_groups:
        if len(set(letter_group)) > 1: break
        longest_pre += letter_group[0]
    return longest_pre


def lcp3(strs):
    if not strs:
        return ""

    min_s = min(strs)
    max_s = max(strs)

    if not min_s:
        return ""

    for i in range(len(min_s)):
        if max_s[i] != min_s[i]:
            return max_s[:i]
    return min_s[:]


def lcp4(strs):
    longest_pre = []

    if strs and len(strs) > 0:
        strs = sorted(strs)

        first, last = strs[0], strs[-1]

        for i in range(len(first)):
            if len(last) > i and last[i] == first[i]:
                longest_pre.append(last[i])
            else:
                return "".join(longest_pre)
        return "".join(longest_pre)


if __name__ == '__main__':
    # strings = ["flower", "flight", "flow"]
    strings = ['aaa', 'aa', 'aaa']

    # print(lcp(strings))
    # print(lcp2(strings))

    print(lcp3(strings))
