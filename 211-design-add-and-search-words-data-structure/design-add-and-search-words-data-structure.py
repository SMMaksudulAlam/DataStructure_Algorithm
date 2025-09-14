class WordDictionary:

    def __init__(self):
        self.dic = {}

    def addWord(self, word: str) -> None:
        dic = self.dic
        for ch in word:
            if(ch not in dic):
                dic[ch] = {}
            dic = dic[ch]
        dic['end'] = 1
    
    def search_(self, word: str, dic) -> bool:
        for i, ch in enumerate(word):
            if(ch == '.'):
                for ascii in range(ord('a'), ord('z')+1):
                    if(chr(ascii) in dic):
                        res = self.search_(word[i+1:], dic[chr(ascii)])
                        if(res):
                            return True
                return False
            elif(ch not in dic):
                return False
            else:
                dic = dic[ch]
        if('end' in dic):
            return True
        return False


    def search(self, word: str) -> bool:
        dic = self.dic
        for i, ch in enumerate(word):
            if(ch == '.'):
                return self.search_(word[i:], dic)
            elif(ch not in dic):
                return False
            else:
                dic = dic[ch]
        if('end' in dic):
            return True
        return False




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)