class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie = {}

        for w in words: 
            trie_ = trie 
            for ch in w: 
                if(ch not in trie_):
                    trie_[ch] = {} 
                trie_[ch]['count'] = trie_[ch].get('count', 0) + 1 
                trie_ = trie_[ch]
        
        ans = []
        for w in words:
            trie_ = trie
            count = 0
            for ch in w:
                count += trie_[ch]['count']
                trie_ = trie_[ch]
            ans.append(count)

        return ans