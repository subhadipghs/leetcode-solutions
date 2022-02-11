from calendar import c
from unittest import TestCase
import unittest


class Solution:
    # Naive approach with O(n^2) complexity
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

    # Sliding window principle
    def lengthOfTheLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        charMap = {}
        length = 0
        while True:
            if left >= len(s) or right >= len(s):
                break
            if charMap.get(s[right]) == None:
                charMap[s[right]] = s[right]
                right += 1
            else:
                charMap.pop(s[left])
                left += 1
                range = abs(left - right) + 1
                if range > length:
                    length = range
        return length


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

    def test_4(self):
        self.assertEqual(
            self.solution.lengthOfTheLongestSubstring(" "), 1)


if __name__ == "__main__":
    unittest.main()
