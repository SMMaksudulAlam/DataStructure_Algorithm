class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        dic = self.trie
        for ch in word:
            if(ch not in dic):
                dic[ch] = {}
            dic = dic[ch]
        dic["end"] = word
        return

    def search(self, word: str) -> bool:
        dic = self.trie

        def srch(dic, w):
            if(not dic):
                return False
            if(not w):
                if("end" in dic):
                    return True
                return False
            
            if(w[0] != '.'):
                if(w[0] not in dic):
                    return False
                return srch(dic[w[0]], w[1:])
            else:
                ans = False
                for key, val in dic.items():
                    if(key == "end"):
                        continue
                    ans = ans or srch(val, w[1:])
                    if(ans):
                        return ans
                return ans

        return srch(dic, word)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)