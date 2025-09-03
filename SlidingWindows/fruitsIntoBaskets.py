class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        start = 0
        ans = 0
        # end is i
        for end in range(0, len(fruits)):
            type_ = fruits[end]
            # expand
            if type_ in d:
                d[type_]+=1
            else:
                d[type_]=1

            #shrinking
            while len(d) > 2:
                d[fruits[start]] -= 1
                if d[fruits[start]] == 0:
                    del d[fruits[start]]
                
                start+=1

            #update the ans
            # what is the count of fruits:
            curr_range = end-start+1 # this is the count of fruits holded by ur window
            ans = max(ans, curr_range)

        return ans
