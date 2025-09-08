class Solution:
    def findPages(self, arr, k):
        # code here
        # start = max of the array
        # end = sum of the array
        if len(arr) < k:
            return -1
            
        def check(mid):
            # check whether i can distribute books such that max is less than mid
            students_taken = 1
            pages = 0
            for x in arr:
                if pages + x <=mid:
                    pages+=x
                else:
                    # you want a new person
                    students_taken+=1
                    pages = x
                    
            if students_taken <=k :
                return True
            else:
                return False
            
# pages=90, mid=100, x=90, students=2

        start = max(arr)
        end = sum(arr)
        ans = -1
        while start<=end:
            mid = (start+end)//2
            # print(mid)
            if check(mid) == True:
                # print("in if")
                ans= mid
                # all the bigger values will also be true
                # but we want a smaller on
                # so shifting ss to left
                end = mid-1
            else:
                # print("in else")
                # all smaller values also will be false
                # so i want a bigger limit
                # i have to go to right 
                start = mid+1
                
        return ans


#  [12, 34, 67, 90]
#  k=4
#  sum = 270
# 90 to 270
# 1 to 1000000
# upper cap = 10
# A, B
# A = 12
# B = 34+67+90 =191 
# in allocation1: max is 191

# A = 12+34+67 =113 
# B = 90
# in allocation2: max is 113

# A = 12+34 = 46
# B = 67+90 =157 
# in allocation3: max is 157

# //ans will stleast be 12
# //ans at max can be sum of all
# 90 to 250(sum of all)

# mid=200(possible) then i saved it and shifted to left
# ans=200
# a=12+34+67=113 
# b=90

# mid=100(not possible, so lesser also not possible, shift to right)
# a=12+34=46 
# b=67
# c = 90

# - - - - - - - - - - - - 
# a=12
# b=34
# c=67
# d=90

# k <4
