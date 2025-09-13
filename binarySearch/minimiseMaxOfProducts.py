class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def check(mid):
            shops_used=0
            for x in quantities:
                # if i have i-th product 11, mid=5
                # 11/5 = 2, +1
                shops_used += x//mid
                if x%mid:
                    shops_used+=1
            
            if shops_used<=n:
                return True
            return False

        start = 1
        end = max(quantities)
        ans = 0

        while start<=end:
            mid = (start+end)//2 #how much max some shop is going to get (x)
            if check(mid)==True:
                ans=mid
                end = mid-1
            else:
                start = mid+1

        return ans


#  11 6 - - - -
#  x=11
#  minimise this x = ans

# is it a binary search on ans
# what will be the search space=> see what is asked?
# what would be the end points=> take the larger if not specific
# how do u validate the mid ####q => depends on the ques
# how do you check -> how u code => implementation logic

