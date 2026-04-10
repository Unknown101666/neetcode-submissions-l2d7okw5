class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r , maxm = 0 , len(heights)-1 , 0
        while l<r:
            a = min(heights[l],heights[r])
            calarea = a*abs(l-r)
            maxm = max(calarea, maxm )
            if heights[l] <= heights[r]:
                l+=1
                
            elif heights[l] >= heights[r]:
                r-=1
        return maxm    

                

        