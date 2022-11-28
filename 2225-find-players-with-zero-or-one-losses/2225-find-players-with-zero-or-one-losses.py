class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = defaultdict(int)
        for winner,loser in matches:
            winners.add(winner)
            losers[loser] += 1
        res1 = []
        res2 = []
        for winner in winners:
            if winner not in losers:
                res1.append(winner)
        for loser in losers:
            if losers[loser] == 1:
                res2.append(loser)
        res1.sort()
        res2.sort()
        return [res1,res2]
        