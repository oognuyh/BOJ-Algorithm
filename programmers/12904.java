/*
 * 12904. 가장 긴 팰린드롬
 */
class Solution {
    public int solution(String s) {        
        int maximum = 1;
        
        for (int i = 0; i < s.length() - 1; i++) {
            maximum = Math.max(maximum, Math.max(expand(s, i, i + 1), expand(s, i, i + 2)));
        }
        
        return maximum;
    }
    
    public int expand(String s, int left, int right) {
        while (0 <= left && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        
        return right - left - 1;
    }
}