/*
 * 84512. 모음 사전
*/
class Solution {
    static final String[] ALPHABETS = {"A", "E", "I", "O", "U"};
    static boolean isFound = false;
    static int count = 0;
    static String target;

    public int solution(String word) {
        target = word;

        permutation(new StringBuilder());

        return count;
    }

    public void permutation(StringBuilder candidate) {
        if (candidate.length() > 5) {
            count--;
        } else {
            if (target.equals(candidate.toString())) 
                isFound = true;

            for (var alphabet : ALPHABETS) {
                if (isFound) continue;

                candidate.append(alphabet);
                count++;

                permutation(candidate);

                candidate.deleteCharAt(candidate.length() - 1);
            }
        }
    }
}