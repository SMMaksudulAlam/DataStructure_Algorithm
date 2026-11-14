# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        #{ind: {sim_score: set()}}
        #{e: ind}

        dic = {i: {} for i in range(len(words))}
        ind = {}

        def sim(w1, w2):
            count = 0
            for i in range(len(w1)):
                if(w1[i] == w2[i]):
                    count += 1
            return count

        for i in range(len(words)):
            w1 = words[i]
            ind[w1] = i

            for j in range(i+1, len(words)):
                w2 = words[j]
                sim_score = sim(w1, w2)

                sub = dic[i]
                if(sim_score not in sub):
                    sub[sim_score] = set()
                sub[sim_score].add(w2)

                sub = dic[j]
                if(sim_score not in sub):
                    sub[sim_score] = set()
                sub[sim_score].add(w1)


        
        track_score = {}
        def dfs(w, p):
            sim_score = master.guess(w)
            track_score[w] = sim_score
            if(sim_score == 6):
                return True
            
            index = ind[w]
            next_set = dic[index].get(sim_score, set())
            if(not next_set):
                return False
            for next_w in next_set:
                if(next_w == p):
                    continue
                all_matched = True
                for k, v in track_score.items():
                    if(sim(next_w, k) != v):
                        all_matched = False
                        break
                if(all_matched):
                    return dfs(next_w, w)
            return False

        if(dfs(words[0], "")):
            return "You guessed the secret word correctly."
        
        return "Either you took too many guesses, or you did not find the secret word."