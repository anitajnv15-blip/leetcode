class Solution(object):
    def isPerfectSquare(self, num):
        left = 1
        right = num 
        while left <= right:
            mid = (left+right)//2
            square = mid*mid
            if num == square:
                return True
            elif num < square:
                right = mid -1
            else:
                left = mid + 1
        return False
        
            