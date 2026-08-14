class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        oldkey=1
        key=1
        if not nums :
            return 0
        if len(nums)==1:
            return 1    
        for i in range(1,len(nums)):
            if (nums[i]-nums[i-1])==1 or nums[i]==nums[i-1]:
                if nums[i]==nums[i-1]:
                    continue 
                key+=1
            else:
                if oldkey<=key:
                    oldkey=key
                    key=1
            if oldkey<=key:
                    oldkey=key    
        return oldkey               