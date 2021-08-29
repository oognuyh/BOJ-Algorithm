/*
 *  12924. 숫자의 표현
 */
import java.util.stream.IntStream;

class Solution {
    public int solution(int n) {
        return (int) IntStream
            .rangeClosed(1, n / 2)
            .filter(i -> {
                int sum = 0;
                
                while (sum < n) 
                    sum += i++;
                
                return sum == n ? true : false;
            })
            .count() + 1;
    }
}
/*
 * # Others
 *      1. 주어진 자연수를 연속된 자연수의 합으로 표현하는 방법의 수는 주어진 수의 홀수 약수의 개수와 같다
 *          int answer = 0;
 *          for (int i = 1; i <= num; i += 2) {
 *              if (num % i == 0) {
 *                  answer++;
 *              }
 *          }
 *          return answer;
 */