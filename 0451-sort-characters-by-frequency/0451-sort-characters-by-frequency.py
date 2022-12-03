class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        lst = [[freq[i],i] for i in freq]
        lst.sort(reverse=True)
        return "".join([i[0]*i[1] for i in lst])