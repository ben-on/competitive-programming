class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        st ={i for i in range(n)}
        for fromi, toi in edges:
            if toi in st:
                st.remove(toi)
        return list(st)