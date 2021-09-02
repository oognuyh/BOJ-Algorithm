/*
 * 12973. 짝지어 제거하기
 */
import java.util.Stack;

class Solution {
    public int solution(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char character : s.toCharArray()) {            
            if (stack.empty()) {
                stack.push(character);
            } else {
                if (stack.peek() == character) {
                    stack.pop();
                } else {
                    stack.push(character);
                }
            }
        }
        
        return stack.empty() ? 1 : 0;
    }
}