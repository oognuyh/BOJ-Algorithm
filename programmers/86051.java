/*
 * 86501. 없는 숫자 더하기
 */

import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        return 45 - Arrays.stream(numbers)
            .sum();
    }
}