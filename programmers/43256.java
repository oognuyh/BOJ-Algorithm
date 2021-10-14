/*
 * 43256. 징검다리
 */
import java.util.Arrays;

class Solution {    
    public int solution(int distance, int[] rocks, int n) {        
        int left = 1, right = distance, mid;
        int answer = 0;
        
        Arrays.sort(rocks);
        
        while (left <= right) {
            mid = (left + right) / 2;
            int numOfRemoved = 0, prev = 0;
            
            for (var rock : rocks) {
                if (rock - prev < mid) {
                    numOfRemoved++;
                } else {
                    prev = rock;
                }
            }
            
            if (distance - prev < mid) {
                numOfRemoved++;
            }
            
            if (numOfRemoved <= n) {
                left = mid + 1;
                if (answer < mid) {
                    answer = mid;
                }
            } else {
                right = mid - 1;
            }
        }
        
        return answer;
    }
}
