class Solution:
    def differByOne(self, dict: list[str]) -> bool:
        """
        store = set()
        if(not dict):
            return False
        w_ln = len(dict[0])

        for w in dict:
            for i in range(w_ln):
                w_ = w[:i]+'*'+w[i+1:]
                if(w_ in store):
                    return True
                store.add(w_)

        return False
        """

        store = set()
        if(not dict):
            return False
        w_ln = len(dict[0])
        mod = 10**10 + 7

        p = [1]*w_ln

        for i in range(1, w_ln):
            p[i] = (p[i-1]*26) % mod

        def hash_(w):
            ans = 0
            for i in range(len(w)):
                ch = w[i]
                n = ord(ch) - ord('a')
                ans = (ans + n*p[i]) % mod
            return ans

        for w in dict:
            w_hash = hash_(w)
            for i in range(w_ln):
                ch = w[i]
                n = ord(ch) - ord('a')
                rem_hash = (w_hash - n*p[i]) % mod
                if((i, rem_hash) in store):
                    return True
                store.add((i, rem_hash))
        return False