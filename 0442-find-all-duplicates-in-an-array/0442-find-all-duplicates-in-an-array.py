class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = 0
        ans = []
        while i < n:
            correct_position = arr[i] - 1
            if correct_position != i:
                arr[correct_position], arr[i] = arr[i], arr[correct_position]
                if arr[correct_position] == arr[i]:
                    ans.append(arr[i])
                    i += 1
            else:
                i += 1
        return set(ans)