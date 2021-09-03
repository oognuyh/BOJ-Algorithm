/*
 * 76502. 괄호 회전하기
 */
import java.util.Stack;
import java.util.stream.IntStream;

class Solution {
    public int solution(String s) {
        return IntStream
            .range(0, s.length())
            .map(i -> isRight(i, s))
            .sum();
    }
    
    public int isRight(int i, String s) {
        Stack<Character> stack = new Stack<>();
        s = s.substring(i, s.length()) + s.substring(0, i);
        
        for (char c : s.toCharArray()) {
            if ("({[".contains(c + "")) {
                stack.push(c);
            } else {
                if (stack.empty()) {
                    return 0;
                } else {
                    switch (stack.pop()) {
                        case '[':
                            if (c != ']') return 0;
                            break;
                        case '(':
                            if (c != ')') return 0;
                            break;
                        case '{':
                            if (c != '}') return 0;
                            break;
                    }
                }
            }
        }
        
        return stack.empty() ? 1 : 0;
    }
}
