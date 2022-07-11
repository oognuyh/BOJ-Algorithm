import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {

    private char[][] board;

    private int m;

    private int n;

    private char NONE = '*';

    public boolean canRemove(int x, int y) {
        try {
            if (board[y][x] == NONE)
                return false;
            return board[y][x] == board[y][x + 1] && board[y][x] == board[y + 1][x]
                    && board[y][x] == board[y + 1][x + 1];
        } catch (Exception e) {
            return false;
        }
    }

    public void update() {
        for (int x = 0; x < n; x++) {
            StringBuilder sb = new StringBuilder();

            for (int y = m - 1; y >= 0; y--) {
                if (board[y][x] != NONE) {
                    sb.append(board[y][x]);
                }
            }

            for (int y = sb.length() - 1; y < n; y++) {
                sb.append(NONE);
            }

            for (int y = m - 1; y >= 0; y--) {
                board[y][x] = sb.charAt((m - 1) - y);
            }
        }
    }

    public int solution(int m, int n, String[] board) {
        this.board = Arrays.stream(board)
                .map(String::toCharArray)
                .toArray(char[][]::new);
        this.m = m;
        this.n = n;
        Set<String> possibles = new HashSet<>();
        int numOfRemoved = 0;

        while (true) {
            for (int x = 0; x < n; x++) {
                for (int y = 0; y < m; y++) {
                    if (canRemove(x, y)) {
                        possibles.addAll(
                                List.of(x + "&" + y, (x + 1) + "&" + y, x + "&" + (y + 1), (x + 1) + "&" + (y + 1)));
                    }
                }
            }

            for (var possible : possibles) {
                String[] coord = possible.split("&");
                this.board[Integer.parseInt(coord[1])][Integer.parseInt(coord[0])] = NONE;
            }

            if (possibles.size() == 0)
                break;

            numOfRemoved += possibles.size();
            update();
            possibles.clear();
        }

        return numOfRemoved;
    }
}