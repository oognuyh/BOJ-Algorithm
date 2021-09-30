/*
 * 42897. 도둑질
 */
class Solution {
    public int solution(int[] money) {
        int numOfHomes = money.length;
        int[][] dp = new int[2][numOfHomes];
        
        dp[0][0] = dp[0][1] = money[0];
        dp[1][1] = money[1];
        
        for (int i = 2; i < numOfHomes; i++) {
            dp[0][i] = Math.max(dp[0][i - 2] + money[i], dp[0][i - 1]);
            dp[1][i] = Math.max(dp[1][i - 2] + money[i], dp[1][i - 1]);
        }
        
        return Math.max(dp[0][numOfHomes - 2], 
                        dp[1][numOfHomes - 1]);
    }
}