class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the good half(monotonic half) and based on that divide the array
        start = 0
        end = len(nums)-1
        ans = -1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            else:
                # checking the good half
                if nums[start]>nums[mid]: # making it equal will be wrong
                    # mid to end is good half
                    if target>nums[mid] and target<=nums[end]:
                        start = mid+1
                    else:
                        end = mid-1
                else:
                    #start to mid is the good half
                    if target>=nums[start] and target<nums[mid]:
                        end = mid-1
                    else:
                        start = mid+1
        return -1
            
