class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        p1 = 0
        p2 = n - 1 
        while(p1 < p2):
            if nums[p1] == val and nums[p2] != val:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 -= 1
            elif nums[p1] == val and nums[p2] == val:
                p2 -= 1
            else:
                p1 += 1
        return n - nums.count(val)
