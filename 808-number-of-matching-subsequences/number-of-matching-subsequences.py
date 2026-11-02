class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        w_states = {chr(i): set() for i in range(ord('a'), ord('z')+1)}
        #print(w_states)

        for i, w in enumerate(words):
            w_states[w[0]].add((i, 0)) #w_ind, pointer
        
        count = 0
        for i in range(len(s)):
            ch = s[i]
            elements = w_states[ch]
            w_states[ch] = set()

            for w_ind, p in elements:
                w = words[w_ind]
                p+=1
                if(p == len(w)):
                    count += 1
                else:
                    w_states[w[p]].add((w_ind, p))
        return count
        


