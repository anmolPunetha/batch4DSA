class Solution:
    def aggressiveCows(self, stalls, k):
        # code here
        
        stalls.sort()
        start = 1
        end = stalls[len(stalls)-1] - stalls[0] #last -first
        # end = stalls[len(stalls)-1]
        
        def check(mid):
            cows_placed = 1 # placed first cow at stalls[0]
            last_placed_cow = stalls[0]
            
            for i in range(1, len(stalls)):
                
                if stalls[i] - last_placed_cow >=mid:
                    cows_placed+=1
                    last_placed_cow = stalls[i]
            
            
            if cows_placed>=k:
                return True
            
            return False
        
        ans = 0
        while start<=end:
            mid = (start+end)//2
            if check(mid) == True:
                ans= mid
                start = mid+1 # this will ensure a bigger value is taken next
            else:
                end = mid-1
        
        return ans
        

# #1
# 1 2 4
# the min distance found is 1

# # you have to place cows in such a way that they are as far as possible
# # maximise the min distance
# # maximise the ans

# #2
# 1 8 9 
# still the ans is 1

# # 3
# 2 4 8
# ans 2

# #4
# 1 4 8
# min is 3

# ans=3


# [10, 1, 2, 7, 5], k = 3
# [1, 2, 5, 7, 10]



