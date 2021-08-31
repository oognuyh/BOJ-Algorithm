/*
 * 12939. 최댓값과 최솟값
 */
import java.util.Arrays;
import java.util.IntSummaryStatistics;
import java.util.stream.Stream;

class Solution {
    public String solution(String s) {
        IntSummaryStatistics summaryStatistics = Stream.of(s)
            .flatMap(str -> Arrays.stream(str.split(" ")))
            .mapToInt(Integer::parseInt)
            .summaryStatistics();
        
        return summaryStatistics.getMin() + " " + summaryStatistics.getMax();
    }
}