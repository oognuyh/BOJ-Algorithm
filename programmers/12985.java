/*
 * 12985. 예상 대진표
 */
class Solution {
    public int solution(int n, int a, int b) {
        int round = 0;

        while (a != b) {
            a = (int) Math.ceil(a / 2f);
            b = (int) Math.ceil(b / 2f);
            round++;
        }        

        return round;
    }
}