# Problem: https://leetcode.com/problems/01-matrix/description/

class Solution:
    def bfs(self, mat: list[list[int]], i: int, j: int) -> int:
        # make BFS
        start_i, start_j = i, j
        q = [(i, j)]
        while q:
            i, j = q.pop(0)
            for x, y in [(j, i + 1), (j, i-1), (j+1, i), (j-1, i)]:
                if 0<= y < len(mat) and 0<= x < len(mat[0]):
                    if abs(start_i-y) + abs(start_j-x) < mat[y][x]:
                        mat[y][x] = abs(start_i-y) + abs(start_j-x)
                        q.append((y, x))

        return mat

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # make BFS
        ans = [[10**4]* len(mat[0]) for _ in range(len(mat))]
        queue = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    ans[i][j] = 0

        while queue:
            i, j, d = queue.pop(0)
            for x, y in [(j, i + 1), (j, i-1), (j+1, i), (j-1, i)]:
                if 0<= y < len(mat) and 0<= x < len(mat[0]):
                    if d+1 < ans[y][x]:
                        ans[y][x] = d+1
                        queue.append((y, x, d+1))

        print(ans)
        return ans
Solution().updateMatrix([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]])