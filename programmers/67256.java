/*
 * 67256. 키패드 누르기
 */
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    int[] current = {10, 12}; // current left & right locations

    public String solution(int[] numbers, String hand) {    
        return Arrays.stream(numbers)
            .mapToObj(number -> {
                switch (number) {
                    case 1:
                    case 4:
                    case 7: 
                        return move(0, number);
                    case 3:
                    case 6:
                    case 9: 
                        return move(1, number);
                    default: 
                        if (number == 0) number = 11;

                        int diff = getDistance(current[0], number) - getDistance(current[1], number);
                        if (diff == 0) { 
                            return move(hand.startsWith("l") ? 0 : 1, number);
                        } else if (diff < 0) { 
                            return move(0, number);
                        } else {
                            return move(1, number);
                        }
                } 
            })
            .collect(Collectors.joining());
    }

    public int getDistance(int from, int to) {
        return Math.abs(--from / 3 - --to / 3) + Math.abs(from % 3 - to % 3);
    }

    public String move(int target, int to) {
        current[target] = to;
        return target == 0 ? "L" : "R";
    }
}