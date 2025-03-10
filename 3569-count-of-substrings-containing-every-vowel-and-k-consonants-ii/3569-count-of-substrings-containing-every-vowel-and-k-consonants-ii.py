class Solution:
    def lessk(self, word, k):
        n = len(word)
        vowels = {'a', 'e', 'i', 'o','u'}

        cnt = 0
        dic = {}  
        ans = 0
        l = 0

        for r in range(n):
            if word[r] in vowels:
                dic[word[r]] = dic.get(word[r], 0) + 1
            else:
                cnt += 1
            
            while len(dic) == 5 and cnt >= k:
                ans += n - r 
                if word[l] in vowels:
                    dic[word[l]] -= 1
                    if dic[word[l]] == 0:
                        del dic[word[l]]
                else:
                    cnt -= 1
                
                l += 1
        
        return ans


    def countOfSubstrings(self, word: str, k: int) -> int:
            return self.lessk(word,k) - self.lessk(word, k + 1)
