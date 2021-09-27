/*
 * 42890. 후보키
 */
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.IntStream;

class Solution {
    List<Integer> candidateKeys = new ArrayList<>();
    
    public int solution(String[][] relation) {
        int numOfStudents = relation.length;
        int numOfAttributes = relation[0].length;
        
        return (int) IntStream
            .range(1, 1 << numOfAttributes)
            .filter(this::isMinimality)
            .filter(i -> {
                Set<String> set = new HashSet<>();
                
                for (int j = 0; j < numOfStudents; j++) {
                    StringBuilder key = new StringBuilder();
                    
                    for (int k = 0; k < numOfAttributes; k++) {
                        if (((1 << k) & i) > 0) key.append(relation[j][k]).append(" ");
                    }
                    
                    if (!set.add(key.toString())) break;
                }
                
                if (set.size() == numOfStudents) {
                    candidateKeys.add(i);
                    return true;
                } else {
                    return false;
                }
            })
            .count();
    }
    
    boolean isMinimality(int i) {
        return candidateKeys.stream()
            .noneMatch(key -> (key & i) == key);
    }
}