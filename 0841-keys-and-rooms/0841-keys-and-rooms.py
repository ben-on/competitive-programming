class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stk = [0]
        vis = {0}
        while stk:
            temp = stk.pop()
            for nb in rooms[temp]:
                if nb not in vis:
                    stk.append(nb)
                    vis.add(nb)
        return len(vis) == len(rooms)