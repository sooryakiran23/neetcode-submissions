class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right=len(heights)-1
        left=0
        best=0
        while left<right:
            k=right-left
            v=min(heights[right],heights[left])
            x=k*v
            if x>best:
                best=x
            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1
        return best                
        