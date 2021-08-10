/*
 * 83201. 상호 평가
 */
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public String solution(int[][] scores) {
        int NUM_OF_STUDENTS = scores.length;
        double[] students = new double[NUM_OF_STUDENTS];
        
        scores = convert(scores);
        
        for (int i = 0; i < NUM_OF_STUDENTS; i++) {
            int max = Arrays.stream(scores[i]).max().getAsInt();
            int min = Arrays.stream(scores[i]).min().getAsInt();
            boolean isMinOrMax = scores[i][i] == max || scores[i][i] == min;
            
            if (isMinOrMax && isOnly(scores[i], scores[i][i])) {
                scores[i][i] = -1;
            } 
            
            students[i] = Arrays.stream(scores[i])
                .filter(score -> score != -1)
                .average()
                .getAsDouble();
        }
        
        return Arrays.stream(students)
            .mapToObj(student -> {
                if (student >= 90) {
                    return "A";
                } else if (student >= 80) {
                    return "B";
                } else if (student >= 70) {
                    return "C";
                } else if (student >= 50) {
                    return "D";
                } else {
                    return "F";
                }    
            })
            .collect(Collectors.joining());
    }
    
    public boolean isOnly(int[] scores, int value) {
        return Arrays.stream(scores)
            .filter(score -> score == value)
            .count() == 1;
    }
    
    public int[][] convert(int[][] scores) {        
        int[][] convertedScores = new int[scores.length][scores.length];
        
        for (int i = 0; i < scores.length; i++) {
            for (int j = 0; j < scores.length; j++) {
                convertedScores[i][j] = scores[j][i];
            }
        }
        
        return convertedScores;
    }
}