class Solution:
    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for i in strs:
           key = ''.join(sorted(i))
           anagram[key].append(i)
        return list(anagram.values())          
                    

