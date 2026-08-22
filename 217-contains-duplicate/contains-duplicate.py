class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for value in nums:
            seen[value] = seen.get(value,0)+1
            if seen[value] > 1: 
                return True

        return False
