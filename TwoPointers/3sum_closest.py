class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #sort the list
        nums.sort()
        min_diff = float("inf")
        ans = 0
        for a in range(len(nums)):
            new_target = target - nums[a]
            # b+c = new_target
            start = a+1
            end = len(nums)-1
            while start<end:
                curr_triplet_sum = nums[a] + nums[start] + nums[end]
                if abs(curr_triplet_sum-target) < min_diff:
                    #closer element
                    min_diff = abs(curr_triplet_sum-target)
                    ans = curr_triplet_sum

                curr_sum = nums[start] + nums[end]
                if curr_sum == new_target:
                    return target
                elif curr_sum <new_target:
                    start+=1
                else:
                    end-=1
        
        return ans
        
