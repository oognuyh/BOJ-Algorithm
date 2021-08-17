/*
 * 42898. 등굣길
 */
class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] board = new int[n][m];
        int PUDDLE = -1;
        
        board[0][0] = 1;
        for (var puddle : puddles) {
            board[puddle[1] - 1][puddle[0] - 1] = PUDDLE;
        }
        
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                if (board[y][x] == PUDDLE) {
                    board[y][x] = 0;
                } else {
                    if (y > 0) {
                        board[y][x] += board[y - 1][x];
                    } 
                    if (x > 0) {
                        board[y][x] += board[y][x - 1];
                    }
                    board[y][x] %= 1000000007;
                }
            }
        }
        
        return board[n - 1][m - 1];
    }
}