/*
 * 12913. 땅따먹기
 */
import java.util.Arrays;

class Solution {    
    int solution(int[][] land) {
        for (int y = 1; y < land.length; y++) {
            land[y][0] += Math.max(land[y - 1][1], Math.max(land[y - 1][2], land[y - 1][3]));
            land[y][1] += Math.max(land[y - 1][0], Math.max(land[y - 1][2], land[y - 1][3]));
            land[y][2] += Math.max(land[y - 1][0], Math.max(land[y - 1][1], land[y - 1][3]));
            land[y][3] += Math.max(land[y - 1][0], Math.max(land[y - 1][1], land[y - 1][2]));
        }
        
        return Arrays.stream(land[land.length - 1])
            .max()
            .getAsInt();
    }
}