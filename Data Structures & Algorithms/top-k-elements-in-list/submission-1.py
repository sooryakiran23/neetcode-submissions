class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new=[]
        g=Counter(nums)
        mostcommon = g.most_common(k)
        return [num for num,freq in mostcommon]