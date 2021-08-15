/*
 * 43238. 입국심사
 */
import java.util.Arrays;

class Solution {
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        long left = 0L;
        long right = times[times.length - 1] * (long) n;
        long answer = 0L;
        
        while (left <= right) {
            long mid = (left + right) / 2;
            long sum = 0;
            
            for (var time : times) {
                sum += mid / time;
            }
            
            if (sum < n) {
                left = mid + 1;
            } else {
                right = mid - 1;
                answer = mid;
            }
        }
        
        return answer;
    }
}