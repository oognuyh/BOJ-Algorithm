/*
 * 72412. 순위 검색
 */
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    Map<String, List<Integer>> applicants = new HashMap<>();
    
    public int[] solution(String[] info, String[] query) {
        int[] results = new int[query.length];
        for (int i = 0; i < info.length; i++) generate(info[i]);
        
        applicants.entrySet()
            .forEach(entry -> Collections.sort(entry.getValue()));
        
        for (int i = 0; i < query.length; i++) {
            String[] conditions = query[i].split(" ");
            String key = conditions[0] + conditions[2] + conditions[4] + conditions[6];
            int score = Integer.parseInt(conditions[7]);
            
            if (applicants.containsKey(key)) {
                results[i] = getNumOfApplicants(applicants.get(key), score);
            }
        }
        
        return results;
    }
    
    void generate(String info) {
        String[] applicant = info.split(" ");
        String[] languages = { applicant[0], "-" };
        String[] jobs = { applicant[1], "-" };
        String[] careers = { applicant[2], "-" };
        String[] foods = { applicant[3], "-" };
        int score = Integer.parseInt(applicant[4]);
        
        for (var language : languages) {
            for (var job : jobs) {
                for(var career : careers) {
                    for (var food : foods) {
                        applicants.computeIfAbsent(language + job + career + food,
                                                   key -> new ArrayList<Integer>()).add(score);
                    }
                }
            }
        }
    }
    
    int getNumOfApplicants(List<Integer> scores, int score) {
        int start = 0, mid = 0, end = scores.size();
        
        while (end > start) {
            mid = (start + end) / 2;
            
            if (scores.get(mid) >= score) end = mid;
            else start = mid + 1;
        }
        
        return scores.size() - start;
    }
}