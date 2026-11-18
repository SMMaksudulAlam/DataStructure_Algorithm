class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        wrds = {}
        for w in words:
            wrds[w] = wrds.get(w, 0) + 1
        
        arr = [0]*len(s)
        w_len = len(words[0])
        for i in range(len(s)):
            if(s[i:i+w_len] in wrds):
                arr[i] = 1

        ans = []
        perm_len = w_len*len(words)
        for i in range(len(s)):
            if(arr[i] == 1):
                dic = {}
                ind = i
                limit = min(i + perm_len, len(s))
                while(ind<limit):
                    if(arr[ind] == 1):
                        sub = s[ind:ind+w_len]
                        if(sub in wrds):
                            dic[sub] = dic.get(sub, 0) + 1
                        else:
                            break
                    else:
                        break
                    ind += w_len

                matched = True
                for w, v in wrds.items():
                    if(w not in dic or dic[w]!=v):
                        matched = False
                        break
                if(matched):
                    ans.append(i)

        return ans

        #TC --> O(n*w*w_len)
        """
        #previous approach gets TLE
        #at the beginning i was planning to run a sliding window, but held on because i though the a correct word sequence can start from any index, starting from 0 with w_len jump might not catch them
        #so, the solution to this problem is we will iterate over range(0--len(w)) to capture all possible index of s where the result sequence start from.

        wrds = {}
        for w in words:
            wrds[w] = wrds.get(w, 0) + 1

        w_len = len(words[0])
        words_count = len(words)
        ans = []

        for start in range(w_len):
            right = start
            left = start
            dic = {}
            count = 0

            while(right < len(s)):
                sub = s[right:right+w_len]
                if(sub in wrds):
                    dic[sub] = dic.get(sub, 0) + 1
                    count += 1

                    while(dic[sub]>wrds[sub]):
                        left_sub = s[left:left+w_len]
                        dic[left_sub] -= 1
                        count -=1
                        left += w_len

                    if(count == words_count):
                        ans.append(left)
                else:
                    left = right+w_len
                    count = 0
                    dic = {}
                right += w_len

        return ans

        #TC --> O(w_len*n)