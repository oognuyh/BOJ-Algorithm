/*
 * 87377. 교점에 별 만들기
 */
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    class Point {
        long x;
        long y;

        public Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }

    public String[] solution(int[][] line) {
        Point maximum = new Point(Long.MIN_VALUE, Long.MIN_VALUE);
        Point minimum = new Point(Long.MAX_VALUE, Long.MAX_VALUE);
        Set<Point> points = new HashSet<>();

        for (int i = 0; i < line.length - 1; i++) {
            long a = line[i][0];
            long b = line[i][1];
            long e = line[i][2];

            for (int j = i + 1; j < line.length; j++) {
                long c = line[j][0];
                long d = line[j][1];
                long f = line[j][2];

                if (!isValid(a, b, e, c, d, f)) continue;

                Point point = new Point(
                    (b * f - e * d) / (a * d - b * c), 
                    (e * c - a * f) / (a * d - b * c)
                );

                points.add(point);
                maximum.x = Math.max(maximum.x, point.x);
                maximum.y = Math.max(maximum.y, point.y);
                minimum.x = Math.min(minimum.x, point.x);
                minimum.y = Math.min(minimum.y, point.y);
            }
        }
        int height = (int) (maximum.y - minimum.y + 1);
        int width = (int) (maximum.x - minimum.x + 1);

        char[][] answer = new char[height][width];
        Arrays.stream(answer)
            .forEach(row -> Arrays.fill(row, '.'));

        points.forEach(p -> answer[(int) (maximum.y - p.y)][(int) (p.x - minimum.x)] = '*');

        return Arrays.stream(answer)
            .map(String::new)
            .toArray(String[]::new);
    }

    boolean isValid(long a, long b, long e, long c, long d, long f) {
        return (a * d - b * c != 0) && 
               ((b * f - e * d) % (a * d - b * c) == 0) &&
               ((e * c - a * f) % (a * d - b * c) == 0);
    }
}