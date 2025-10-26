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