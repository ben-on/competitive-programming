class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]

        for seq in arr:
            chars = set(seq)

            if len(chars) < len(seq):
                continue

            dp.extend(chars | other for other in dp if not (chars & other))

        return max(map(len, dp))