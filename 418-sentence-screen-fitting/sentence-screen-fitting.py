class Solution:
    def wordsTyping(self, sentence: list[str], rows: int, cols: int) -> int:
        """
        count = 0
        ind = 0
        for i in range(rows):
            col = 0
            while(col + len(sentence[ind]) - 1 <cols):
                col += len(sentence[ind]) + 1 
                ind += 1
                if(ind == len(sentence)):
                    count +=1 
                    ind = 0
        return count
        """

        buffer = 0
        s = " ".join(sentence) + " "
        ln = len(s)
        for i in range(rows):
            buffer += cols
            ind = (buffer % ln) - 1
            if(s[ind]==' '):
                continue
            if(s[ind+1]==' '):
                buffer += 1
                continue
            while(ind>=0 and s[ind]!=' '):
                ind-=1
                buffer-=1
        return buffer // ln