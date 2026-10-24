class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
      sumA = sum(aliceSizes)
      sumB = sum(bobSizes)
      difference = (sumA-sumB)//2
      bobSet = set(bobSizes)
      for x in aliceSizes:
        y = x-difference
        if y in bobSet:
            return[x,y]