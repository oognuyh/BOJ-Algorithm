/*
 * 68645. 삼각 달팽이
 */
import java.util.Arrays;

class Solution {
    public int[] solution(int n) {
        int[][] grid = new int[n][n];
        int x = 0, y = -1, number = 1;
        
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (i % 3 == 0) grid[++y][x] = number++;
                else if (i % 3 == 1) grid[y][++x] = number++;
                else grid[--y][--x] = number++;
            }
        }
        
        return Arrays.stream(grid)
            .flatMapToInt(row -> Arrays.stream(row))
            .filter(num -> num != 0)
            .toArray();
    }
}