/*
 * 12981. 영어 끝말잇기
 */
import java.util.HashSet;
import java.util.Set;

class Solution {
    public Set<String> usedWords = new HashSet<>();
    
    public int[] solution(int n, String[] words) {
        usedWords.add(words[0]);
        
        for (int i  = 1; i < words.length; i++) {
            if (!isConnected(words[i - 1], words[i]) || isDuplicate(words[i])) {
                return new int[] {(i % n) + 1, (i / n) + 1};
            } 
            usedWords.add(words[i]);
        }
        return new int[] {0, 0};
    }
    
    public boolean isConnected(String previousWord, String currentWord) {
        return previousWord.charAt(previousWord.length() - 1) == currentWord.charAt(0);
    }
    
    public boolean isDuplicate(String word) {
        return usedWords.contains(word);
    }
}