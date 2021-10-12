/*
 * 17676. 추석 트래픽
 */
import java.sql.Timestamp;
import java.util.Arrays;

class Solution {
    class Time {
        long start;
        long end;

        public Time(String line) {
            String[] t = line.split(" ");

            end = Timestamp.valueOf(t[0] + " " + t[1]).getTime();
            start = end - (long) (Double.parseDouble(t[2].replace("s", "")) * 1000) + 1;
        }
    }

    boolean isIncluded(long start, long end, Time time) {
        return (time.start >= start && time.start < end)
            || (time.end >= start && time.end < end)
            || (time.start <= start && time.end >= end);
    }

    int count(long start, long end, Time[] times) {
        int num = 0;

        for (var time : times) 
            if (isIncluded(start, end, time)) num++;

        return num;
    }

    public int solution(String[] lines) throws Exception {
        int maximum = Integer.MIN_VALUE;
        Time[] times = Arrays.stream(lines)
            .map(Time::new)
            .toArray(Time[]::new);

        for (var time : times) 
            maximum = Math.max(maximum, Math.max(count(time.start, time.start + 1000, times), count(time.end, time.end + 1000, times)));

        return maximum;
    }
}