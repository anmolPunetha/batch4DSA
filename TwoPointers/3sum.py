#https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort
        #3sum logic:
            # assuming a number and applying 2sum
        
        nums.sort()
        print(nums)
        result = []
        for a in range(len(nums)):
            if a>0 and nums[a]==nums[a-1]:
                continue
                #case1 of duplicacy: same a is coming and it may give same triplets
            new_target = 0 - nums[a]
            # b+c = new_target
            start = a+1
            end = len(nums)-1
            while start<end:
                curr_sum = nums[start] + nums[end]
                
                if curr_sum == new_target:
                    result.append([nums[a], nums[start], nums[end]])
                    # now lets go to a new value, case#2
                    org_val = nums[start]
                    while start<end and nums[start] == org_val:
                        #skip all those values
                        start+=1
                elif curr_sum <new_target:
                    start+=1
                else:
                    end-=1
        
        return result
