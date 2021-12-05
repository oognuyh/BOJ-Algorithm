/*
 * 77884. 약수의 개수와 덧셈
 */
import java.util.stream.IntStream;

class Solution {
    public int solution(int left, int right) {        
        return IntStream
            .rangeClosed(left, right)
            .map(number -> number % Math.sqrt(number) == 0 ? -number : number)
            .sum();
    }
}