/*
 * 12909. 올바른 괄호
 */
import java.util.Stack;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (var character : s.toCharArray()) {
            if (character == '(') {
                stack.push(character);
            } else {
                if (stack.empty()) {
                    return false;
                } else {
                    stack.pop();
                }
            }
        }
        
        return stack.empty() ? true : false;
    }
}