class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i,j,ans = 0,0,[]
        
        while i<len(firstList) and j<len(secondList):
            start1 = firstList[i][0]
            end1 = firstList[i][1]
            start2 = secondList[j][0]
            end2 = secondList[j][1]
            if(start1<=start2):
                if(end1>=start2):
                    s=max(start1,start2)
                    e = min(end1,end2)
                    ans.append([s,e])
            else:
                if(start2<=start1):
                    if(end2>=start1):
                        s = max(start1,start2)
                        e = min(end1,end2)
                        ans.append([s,e])
            if(end1<=end2):
                i+=1
            else:
                j+=1
        return ans 
       