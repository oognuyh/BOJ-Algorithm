/*
 * 67257. 수식 최대화
 */
import java.util.stream.IntStream;

class Solution {
    public long solution(String expression) {
        String[][] operations = {
            {"+", "-", "*"},
            {"+", "*", "-"},
            {"-", "+", "*"},
            {"-", "*", "+"},
            {"*", "-", "+"},
            {"*", "+", "-"}
        };
        
        return IntStream
            .range(0, operations.length)
            .mapToLong(i -> {
                String[] first = expression.split("\\" + operations[i][0]);
                
                for (int j = 0; j < first.length; j++) {
                    String[] second = first[j].split("\\" + operations[i][1]);
                    
                    for (int k = 0; k < second.length; k++) 
                        second[k] = String.valueOf(operate(second[k].split("\\" + operations[i][2]), operations[i][2]));
                    
                    first[j] = String.valueOf(operate(second, operations[i][1]));
                }
                
                return Math.abs(operate(first, operations[i][0]));
            })
            .max()
            .getAsLong();
    }
    
    public long operate(String[] numbers, String operation) {
        long total = Long.valueOf(numbers[0]);
        
        for (int i = 1; i < numbers.length; i++) {
            if (operation.equals("*")) total *= Long.valueOf(numbers[i]);
            else if (operation.equals("+")) total += Long.valueOf(numbers[i]);
            else if (operation.equals("-")) total -= Long.valueOf(numbers[i]);
        }
        
        return total;
    }
}