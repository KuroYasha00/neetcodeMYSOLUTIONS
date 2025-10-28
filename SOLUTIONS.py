#contains duplicate solution

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = set()
        for num in nums:
            if num in dupe:
                return True
            dupe.add(num)
        return False
    nums = [1, 2, 3, 3]
    hasDuplicate(nums)
#IS ANAGRAM solutin
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = list(s)
        tList = list(t)
        if sorted(sList) == sorted(tList):
            return True
        else:
            return False

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dupe = {}

        for i, j in enumerate(nums):
            delta = target - j
            if delta in dupe:
                return[dupe[delta], i]
            dupe[j] = i
