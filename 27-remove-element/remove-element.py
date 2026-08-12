class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        no = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[no] = nums[i]
                no+=1
        return no
                