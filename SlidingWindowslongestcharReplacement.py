class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)

        def isShrinkingReq(d, k, lengthofWindow):
            
            #maxfreq
            max_freq = 0
            for key in d.keys():
                max_freq = max(max_freq, d[key])
            
            req_ops = lengthofWindow - max_freq

            if req_ops > k:
                return True
            else:
                return False

        start = 0
        maxLen = 0
        for end in range(len(s)):
            #expand
            d[s[end]] += 1

            #shrink
            while start<=end and isShrinkingReq(d, k, end-start+1) == True:
                d[s[start]] -= 1
                start+=1

            #update
            currLen = end-start+1
            maxLen = max(maxLen, currLen)
        
        return maxLen
