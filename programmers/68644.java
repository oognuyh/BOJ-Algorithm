/*
 * 68644. 두 개 뽑아서 더하기
 */
import java.util.stream.IntStream;

class Solution {
    public int[] solution(int[] numbers) {
        return IntStream
            .range(0, numbers.length)
            .flatMap(i -> IntStream
                .range(i + 1, numbers.length)
                .map(j -> numbers[i] + numbers[j]))
            .distinct()
            .sorted()
            .toArray();            
    }
}