class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if word[0].isupper() and n > 1:
            # print("yes")
            cur = word[1].isupper()
            for i in range(2,n):
                if word[i].isupper()!=cur:
                    return False
        else:
            for i in range(1,n):
                # print(word[i])
                if word[i].isupper():
                    return False
        return True
            
            
            