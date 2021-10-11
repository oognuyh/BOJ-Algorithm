/*
 * 1829. 카카오프렌즈 컬러링북
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    List<Integer> areas = new ArrayList<>();
    int[] dx = new int[] { -1, 1, 0, 0 };
    int[] dy = new int[] { 0, 0, -1, 1 };
    long[][] grid;
    
    public int[] solution(int m, int n, int[][] picture) {
        grid = Arrays.stream(picture)
            .map(e -> Arrays.stream(e)
                 .asLongStream()
                 .toArray())
            .toArray(long[][]::new);
        
        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                if (grid[y][x] != 0) { 
                    areas.add(0);
                    extend(y, x);
                }
            }
        }        
        
        return new int[] { 
            areas.size(), 
            areas.stream()
                .mapToInt(Integer::intValue)
                .max()
                .getAsInt() 
        };
    }
    
    void extend(int y, int x) {
        long area = grid[y][x];
        grid[y][x] = 0;
        areas.set(areas.size() - 1, areas.get(areas.size() - 1) + 1);
        
        for (int i = 0; i < 4; i++) {
            int nextY = y + dy[i];
            int nextX = x + dx[i];
            
            try {
                if (grid[nextY][nextX] == area) {
                    extend(nextY, nextX);
                }    
            } catch (Exception e) { }
        }
    }    
}