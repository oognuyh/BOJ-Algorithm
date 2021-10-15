/*
 * 12982. 예산
 */
import java.util.Arrays;

class Solution {
    public int solution(int[] d, int budget) {
        int numOfDepts = 0;
        Arrays.sort(d);
        
        for (var _d : d) {
            budget -= _d;
            if (budget < 0) break;

            numOfDepts++;
        }
        
        return numOfDepts;
    }
}