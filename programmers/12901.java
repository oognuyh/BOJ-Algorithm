/*
 * 12901. 2016년
 */
import java.util.stream.IntStream;

class Solution {
    public String solution(int a, int b) {
        String[] dayOfWeek = { "THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED" };
        int[] day = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        
        return dayOfWeek[(IntStream.range(1, a).map(month -> day[month]).sum() + b) % 7];
    }
}