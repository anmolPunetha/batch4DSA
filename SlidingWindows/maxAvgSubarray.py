class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sum of first subarray - O(k)
        curr_sum=0
        for i in range(0,k):
            curr_sum+=nums[i]
        
        ans = curr_sum # if we find a bigger value, we will update max sum (ans)

        for i in range(k, len(nums)):
            # i get a new nu,ber=> end of that subarray
            curr_sum += nums[i] # expansion of window

            curr_sum -= nums[i-k] # contraction of window, this is the number which now should be out

            if curr_sum > ans:
                ans = curr_sum

        max_avg = ans/float(k)
        return max_avg
