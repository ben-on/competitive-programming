class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = 0
        ans = []
        while i < n:
            correct_position = arr[i] - 1
            
            if arr[correct_position] != arr[i]:
                arr[correct_position], arr[i] = arr[i], arr[correct_position]
            else:
                i += 1

        return [arr[i] for i in range(n) if arr[i] != i + 1]