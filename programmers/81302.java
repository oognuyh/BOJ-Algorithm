/*
 * 81302. 거리두기 확인하기
 */
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Objects;
import java.util.Queue;
import java.util.Set;

class Solution {
    class Coord {
        int x, y;

        public Coord(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            Coord another = (Coord) obj;
            return another.x == x && another.y == y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    int[] dx = { 0, 1, 0, -1 };
    int[] dy = { -1, 0, 1, 0 };

    public int[] solution(String[][] places) {
        return Arrays.stream(places)
            .mapToInt(this::isKeeping)
            .toArray();
    }

    int isKeeping(String[] place) {
        for (int y = 0; y < place.length; y++) {
            for (int x = 0; x < place[y].length(); x++) {
                if (place[y].charAt(x) == 'P' && !isValid(place, new Coord(x, y))) {
                    return 0;
                }
            }
        }
        return 1;
    }

    boolean isOutOfRange(Coord coord) {
        return coord.x < 0 || 4 < coord.x || coord.y < 0 || 4 < coord.y;
    }

    int getDistance(Coord c1, Coord c2) {
        return Math.abs(c1.x - c2.x) + Math.abs(c1.y - c2.y);
    }

    boolean isValid(String[] place, Coord start) {
        Queue<Coord> q = new LinkedList<>(List.of(start));
        Set<Coord> already = new HashSet<>(List.of(start));

        while (!q.isEmpty()) {
            Coord cur = q.poll();

            for (int i = 0; i < 4; i++) {
                Coord next = new Coord(cur.x + dx[i], cur.y + dy[i]);

                if (isOutOfRange(next) || 
                    getDistance(start, next) > 2 ||
                    !already.add(next)) continue;

                if (place[next.y].charAt(next.x) == 'O') {
                    q.offer(next);
                } else if (place[next.y].charAt(next.x) == 'P') {
                    return false;
                } 
            }
        }

        return true;
    }
}