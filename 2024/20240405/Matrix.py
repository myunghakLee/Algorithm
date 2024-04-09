# Problem: https://leetcode.com/problems/01-matrix/description/

class Solution:
    def padding(self, mat: list[list[int]], num: int = 9999) -> list[list[int]]:
        cols = len(mat[0])
        zero_row = [num] * (cols + 2)
        
        # 각 행의 양쪽에 0을 추가하고, 상단과 하단에 0으로 이루어진 행을 추가합니다.
        padded_mat = [zero_row] + [[num] + row + [num] for row in mat] + [zero_row]
        
        return padded_mat

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        ans = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        # padding the matrix with 0s
        padded_mat = self.padding(mat)
        print(mat)

        for i in range(len(ans)):
            for j in range(len(ans[0])):
                if ans[i][j] != 0:
                    ans[i][j] = min(padded_mat[i-1][j], padded_mat[i-1][j-2], padded_mat[i][j - 1], padded_mat[i-2][j-1]) + 1
        return ans
    
s = Solution()
print(s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))