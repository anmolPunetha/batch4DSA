class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        def check(mid):
            hrs_req = 0
            for x in piles:
                curr_req = x//mid 
                if x%mid !=0:
                    curr_req+=1
                    
                hrs_req+=curr_req

            if hrs_req<=h:
                return True
            return False

        ans = 0
        while start<=end:
            mid = (start+end)//2
            if check(mid):
                ans = mid
                end = mid-1
            else:
                start = mid+1
        return ans

# [3,6,7,11], h = 8
# start 1 to end 11
# ans = 4

# mid=6 B/hr
# hrs_req = 6hrs <= h

# start=1 , end = 5
# mid=3
# hrs_req = 1+ 2 + 3+ 4 = 10 > h
# i want a greater speed

# start = 4, end = 5
# mid=4
# hrs_req = 8 <=h
# end = 3, start=4
