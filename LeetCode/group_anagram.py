from typing import List


class Solution:
    # My Solve
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = {}
        result = []

        # Key initialized
        for x in set(''.join(sorted(x)) for x in strs):
            answer[x] = []

        for word in strs:
            sortword = ''.join(sorted(word))

            if sortword in answer:
                answer[sortword].append(word)

        for k, v in answer.items():
            result.append(v)

    #     return sorted(result)

    # Refactoring
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     from collections import defaultdict
    #
    #     anagram = defaultdict(list)
    #
    #     for word in strs:
    #         anagram[''.join(sorted(word))].append(word)
    #
    #     return list(anagram.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    obj = Solution()
    print(obj.groupAnagrams(strs))
