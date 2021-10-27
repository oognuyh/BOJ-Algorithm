/*
 * 64061. 크레인 인형뽑기 게임
 */
import java.util.Arrays;
import java.util.Stack;

class Solution {
    int[][] board;
    
    public int solution(int[][] board, int[] moves) {
        Stack<Integer> basket = new Stack<>();
        this.board = board;
        
        return Arrays.stream(moves)
            .map(move -> {
                int doll = getDoll(move - 1);
                if (doll == -1) return 0;
                
                if (!basket.empty() && basket.peek() == doll) {
                    basket.pop();
                    return 2;
                } else {
                    basket.push(doll);
                    return 0;
                }
            })
            .sum();
    }
    
    public int getDoll(int x) {
        for (int y = 0; y < board.length; y++) {
            if (board[y][x] != 0) {
                int doll = board[y][x];
                board[y][x] = 0;
                return doll;
            }
        }
        return -1;
    }
}