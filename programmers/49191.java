/*
 * 49191. 순위
 */
import java.util.stream.IntStream;

class Solution {
    public int solution(int n, int[][] results) {
        boolean[][] didPlay = new boolean[n][n];
        
        for (var result : results) 
            didPlay[result[0] - 1][result[1] - 1] = true;
        
        for (int i = 0; i < n; i++) 
            for (int j = 0; j < n; j++) 
                for (int k = 0; k < n; k++) 
                    if (didPlay[j][i] && didPlay[i][k])
                        didPlay[j][k] = true;
        
        return IntStream
            .range(0, n)
            .map(i -> {
                int numOfGames = 0;
                
                for (int j = 0; j < n; j++)
                    if (didPlay[i][j] || didPlay[j][i]) 
                        numOfGames++;
                
                return numOfGames == n - 1 ? 1 : 0;
            })
            .sum();
    }
}