/*
 * 81301. 숫자 문자열과 영단어
 */
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String s) {
        Map<String, String> mapper = getMapper();
        
        for (String key : mapper.keySet()) {
            s = s.replace(key, mapper.get(key));
        }
        
        return Integer.parseInt(s);
    }
    
    public Map<String, String> getMapper() {
        Map<String, String> mapper = new HashMap<>();
        
        mapper.put("zero", "0");
        mapper.put("one", "1");
        mapper.put("two", "2");
        mapper.put("three", "3");
        mapper.put("four", "4");
        mapper.put("five", "5");
        mapper.put("six", "6");
        mapper.put("seven", "7");
        mapper.put("eight", "8");
        mapper.put("nine", "9");
        
        return mapper;
    }
}