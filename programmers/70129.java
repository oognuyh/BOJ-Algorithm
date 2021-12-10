/*
 * 70129. 이진 변환 반복하기
 */
class Solution {
    public int[] solution(String s) {
        int numOfRemovedZeros = 0, numOfSteps = 0, numOfOnes;

        while (!s.equals("1")) {
            numOfOnes = s.replace("0", "").length();            
            numOfRemovedZeros += s.length() - numOfOnes;

            s = Integer.toBinaryString(numOfOnes);
            numOfSteps++;
        }

        return new int[] { numOfSteps, numOfRemovedZeros };
    }
}