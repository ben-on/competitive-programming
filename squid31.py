class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num=[str(i) for i in num]
        s=list(str(int("".join(num)) + k))
        return [int(i) for i in s]
        
