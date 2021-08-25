/*
 * 62048. 멀쩡한 사각형
 */
import java.math.BigInteger;

class Solution {
    public long solution(int w, int h) {
        int gcd = BigInteger.valueOf(w).gcd(BigInteger.valueOf(h)).intValue();
        
        return (long) w * h - ((long) w + h - gcd);
    }
}