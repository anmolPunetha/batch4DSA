class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #prepare a dict for s1, reference, d1
        #iterate the first window for s2 and save that in d2
        #start your window loop and each char:
            # add the i-th char
            # remove the i-k th char
                # if its freq ==0, delete the key
            #compare d1, d2: return true if they match

        if len(s1)> len(s2):
            return False
        d1 = {}
        k = len(s1)
        for char in s1:
            if char not in d1:
                d1[char]=1
            else:
                d1[char]+=1

        
        d2={}
        
        #sliding window template
        for i in range(0, len(s2)):
            char = s2[i]
            # until i dont have the first k characters
            #expand
            if char not in d2:
                d2[char]=1
            else:
                d2[char]+=1

            #contract
            if i>=k:
                red_char = s2[i-k]
                d2[red_char] -= 1
                if d2[red_char] == 0:
                    del d2[red_char]
            
            #update
            if d1 == d2:
                return True
        
        return False

        
