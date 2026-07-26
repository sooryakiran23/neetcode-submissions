class Solution:

    def encode(self, strs: List[str]) -> str:
        total =""
        for i in strs:
            total+=str(len(i))
            total+='*'    
            total+=i
        return total    

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j].isdigit():
                j += 1

            length = int(s[i:j])

            word = s[j+1 : j+1+length]
            res.append(word)

            i = j + 1 + length

        return res        


