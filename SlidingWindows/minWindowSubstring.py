class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # m1 = A:1, B:1, C:1
        # in m2 I check that: A:0
        if len(s) < len(t):
            return ""

        def check(m1, m2):
            for key in m1.keys(): # m1 will have max 52 entries
                req = m1[key]
                if m2[key] < req:
                    return False
            return True

        # first save t=> M1
        m1 = defaultdict(int)
        for char in t:
            m1[char]+=1

        # how do I save the ans:
        # size and the start
        start = 0
        m2 = defaultdict(int)

        #just to get the max length and its index
        startIdx = -1
        minLen = len(s) + 1
        for end in range(len(s)):
            char = s[end]
            #expansion
            m2[char] +=1 

            #shrink
            while start<=end and m2[s[start]] > m1[s[start]]: # start char is extra
                 m2[s[start]] -= 1
                 start += 1
                
            #update
            if check(m1,m2) == True:
                #update the ans
                currLen = end-start+1
                if currLen < minLen:
                    minLen = currLen
                    startIdx = start
                
        
        # sth as the ans
        if startIdx == -1:
            return ""
        else:
            ans = s[startIdx:startIdx+minLen]
            return ans

# idx=5, length = 5
# s[idx:idx+length]
# m1, m2 should match
# m1 == m2

# m1: 1a, 1b, 1c
# m2: 2d, 1s, 1a, 1b, 1c

# TC: O(N*52)
# SC: O(52)

# s = "ADOBECODEBANC", t = "ABC"
# m1
# 1A, 1B, 1C
# # m1[D] = 0
# m2
# 1A
# 1D
# 1O
# 1B
# 1E
# 1C
