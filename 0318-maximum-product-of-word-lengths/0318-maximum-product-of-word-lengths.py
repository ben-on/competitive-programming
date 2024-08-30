class Solution:
    def maxProduct(self, words: List[str]) -> int:
        new_arr = []

        for word in words:
            newword = 0
            for char in word:
                pos = ord(char) - 97
                newword |= (1 << pos)
            
            new_arr.append(newword)
        
        ans = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and not (new_arr[i] & new_arr[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans


