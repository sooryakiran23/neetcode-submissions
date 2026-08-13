class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        matrixx=[[0 for _ in range(9)] for _ in range(9)]
        text = "".join(element for sublist in board for element in sublist)
        k=0
        for i in range(9):
            for j in range(9):
                matrixx[i][j]=text[k]
                k+=1   
        for i in range(9):
            for j in range(9):
                if matrixx[i][j]==".":
                    continue
                elif matrixx[i][j].isdigit():
                    run=matrixx[i][j]
                    flag=0
                    o=0
                    while o<9:
                        if run==matrixx[i][o] and j!=o:
                            flag=1
                        o+=1        
                    o=0    
                    while o<9:
                        if run==matrixx[o][j] and i!=o:
                            flag=1
                        o+=1        
                    if i ==0 or i==1 or i==2 :
                        k=0
                        h=2
                    elif i ==3 or i==4 or i==5 :
                        k=3
                        h=5
                    else:
                        k=6
                        h=8
                    if j ==0 or j==1 or j==2:
                        c=0
                        n=2
                    elif j ==3 or j==4 or j==5:
                        c=3
                        n=5
                    else:
                        c=6
                        n=8   
                    for v in range(k,h+1):
                        for u in range(c,n+1):
                            if v==i and u==j:
                                continue
                            if run==matrixx[v][u]:
                                flag=1
                    if flag==1:
                        return False
        return True                            


