/*
 * 87389. 나머지가 1이 되는 수 찾기
 */
import java.util.stream.IntStream;

class Solution {
    public int solution(int n) {
        return IntStream
            .rangeClosed(2, (int) Math.sqrt(n - 1))
            .filter(candidate -> (n - 1) % candidate == 0)
            .flatMap(candidate -> IntStream.of(candidate, (n - 1) / candidate))
            .min()
            .orElse(n - 1);
    }
}