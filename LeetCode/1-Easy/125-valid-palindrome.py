"""
Author: jak010
Date: 2021.04.19

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example.
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example.
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        remove_specialized = "".join([x.lower() for x in s if x.isalnum()])
        return remove_specialized == remove_specialized[::-1]

        ## Batter Way 1
        # remove_specialized = "".join([x for x in s if x.isalnum()]).lower()
        # return remove_specialized == remove_specialized[::-1]

        ## Batter Way 2 (other style)
        # remove_specialized = "".join(filter(str.isalnum, s.lower()))
        # return remove_specialized == remove_specialized[::-1]
