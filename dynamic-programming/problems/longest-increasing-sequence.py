from calendar import c
from unittest import TestCase
import unittest


class Solution:
    # Naive approach
    def lengthOfTheLongestSubstringNaive(self, s: str) -> int:
        maxLength = 0  # initial value
        for i in range(len(s)):
            count = 1
            charMap = {
                s[i]: s[i]
            }
            for j in range(i + 1, len(s)):
                # pass
                if charMap.get(s[j]) != None:
                    break
                else:
                    count += 1
                    charMap[s[j]] = s[j]
            charMap = {}
            if count > maxLength:
                maxLength = count
        return maxLength


class TestCases(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(
            self.solution.lengthOfTheLongestSubstring("abcabcbb"), 3)

    def test_2(self):
        self.assertEqual(
            self.solution.lengthOfTheLongestSubstring("bbbbbb"), 1)

    def test_3(self):
        self.assertEqual(
            self.solution.lengthOfTheLongestSubstring("pwwkew"), 3)


if __name__ == "__main__":
    unittest.main()
