
class Solution:
    
    
    def exist(self, board, word):
        NoC = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def DFS(word, x,y):
            if len(word) == 0:
                return True
            elif board[y][x] != word[0]:
                return False

            
            
            
            t_word = board[y][x]
            board[y][x] = False
            for (i,j) in NoC:
                if 0<=x+i < len(board[0]) and 0 <= y+j < len(board):
                    if DFS(word[1:], x+i, y+j):
                        return True
            board[y][x] = t_word
            return False
        
        
        if len(word) == 1 and word[0] == board[0][0]:
            return True
        for i in range(len(board[0])):
            for j in range(len(board)):
                if DFS(word, i, j):
                    return True
        return False
    
