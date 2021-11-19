/*
 * 1837. GPS
 */
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    Map<Integer, Set<Integer>> graph = new HashMap<>();
    final int INF = 987654321;

    public int solution(int n, int m, int[][] edge_list, int k, int[] gps_log) {
        for (var edges : edge_list) {
            graph.computeIfAbsent(edges[0], (key) -> new HashSet<>()).add(edges[1]);
            graph.computeIfAbsent(edges[1], (key) -> new HashSet<>()).add(edges[0]);
        }

        int[][] dp = new int[k][n + 1];
        Arrays.stream(dp)
            .forEach(row -> Arrays.fill(row, INF));

        int startNode = gps_log[0];
        int endNode = gps_log[k - 1];
        dp[0][startNode] = 0;


        for (int i = 1; i < k; i++) {
            for (int node = 1; node < n + 1; node++) {
                dp[i][node] = Math.min(dp[i][node], dp[i - 1][node]);

                for (int nextNode : graph.getOrDefault(node, new HashSet<>())) 
                    dp[i][node] = Math.min(dp[i - 1][nextNode], dp[i][node]);

                dp[i][node] += gps_log[i] == node ? 0 : 1;
            }
        }

        return dp[k - 1][endNode] == INF ?
            -1 :
            dp[k - 1][endNode];
    }
}