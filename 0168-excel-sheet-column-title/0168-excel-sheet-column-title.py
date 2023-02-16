class Solution:
    def convertToTitle(self, num):
        upper = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(upper[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)