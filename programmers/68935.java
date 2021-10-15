/*
 * 68935. 3진법 뒤집기
 */
class Solution {
    public int solution(int n) {
        return Integer.parseInt(new StringBuilder(Integer.toString(n, 3))
            .reverse().toString() , 3);
    }
}