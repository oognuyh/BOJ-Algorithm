/*
 * 49189. 가장 먼 노드
 */
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

class Solution {
    Map<Integer, Set<Integer>> graph = new HashMap<>();
    
    public int solution(int n, int[][] edge) {
        setConnection(n, edge);
        
        Queue<Integer> queue = new LinkedList<>();
        boolean[] isVisited = new boolean[n + 1];
        int numOfFarthestNodes = 0;
        
        queue.offer(1);
        
        while (!queue.isEmpty()) {    
            numOfFarthestNodes = queue.size();
            
            for (int i = 0; i < numOfFarthestNodes; i++) { 
                Integer from = queue.poll(); 
                
                isVisited[from] = true; 
                
                graph.get(from).stream()
                    .filter(to -> !isVisited[to] && !queue.contains(to))
                    .forEach(to -> queue.offer(to)); 
            }
        }
        
        return numOfFarthestNodes;
    }
    
    public void setConnection(int n, int[][] edge) {
        for (int node = 1; node < n + 1; node++) {
            graph.put(node, new HashSet<Integer>());
        }
        
        for (var e : edge) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
    }
}