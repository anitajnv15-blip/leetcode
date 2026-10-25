class Solution(object):
    def specialArray(self, nums):
        nums.sort()
        n = len(nums)
        left = 0
        right = n
        while left <= right:
            x = (left+right)//2
            count = n - self.lower_bound(nums,x)
            if count == x:
                return x
            elif count > x:
                left = x+1
            else:
                right = x-1
        return -1
    def lower_bound(self,nums,target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

