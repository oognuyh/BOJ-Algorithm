/* 
 * 77485. 행렬 테두리 회전하기
 */
class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] result = new int[queries.length];
        int[][] grid = new int[rows][columns];
        
        // initialize the grid
        for (int y = 0; y < rows; y++) {
            for (int x = 0; x < columns; x++) {
                grid[y][x] = (y * columns) + x + 1;
            }
        }
        
        // rotate clockwise
        for (int i = 0; i < result.length; i++) {
            int y1 = queries[i][0], x1 = queries[i][1], y2 = queries[i][2], x2 = queries[i][3];
            int min = grid[y1 - 1][x1 - 1];
            int previous = min;
            
            // →            
            for (int x = x1; x < x2; x++) {                
                int temp = grid[y1 - 1][x];
                if (temp < min) min = temp;
                
                grid[y1 - 1][x] = previous;
                previous = temp;                
            }
            
            // ↓
            for (int y = y1; y < y2; y++) {
                int temp = grid[y][x2 - 1];
                if (temp < min) min = temp;
                
                grid[y][x2 - 1] = previous;
                previous = temp;
            }
            
            // ←
            for (int x = x2 - 2; x1 - 2 < x ; x--) {
                int temp = grid[y2 - 1][x];
                if (temp < min) min = temp;
                
                grid[y2 - 1][x] = previous;
                previous = temp;
            }
            
            // ↑
            for (int y = y2 - 2; y1 - 2 < y ; y--) {
                int temp = grid[y][x1 - 1];
                if (temp < min) min = temp;
                
                grid[y][x1 - 1] = previous;
                previous = temp;
            }            
                     
            result[i] = min;
        }
        
        return result;
    }
}