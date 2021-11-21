/*
 * 87946. 피로도
 */
class Solution {
    boolean[] visited;
    int[][] dungeons;
    int maximum = 0;
    
    public int solution(int k, int[][] dungeons) {
        this.visited = new boolean[dungeons.length] ;
        this.dungeons = dungeons;
        
        explore(k, 0);
        
        return maximum;
    }
    
    void explore(int fatigue, int numOfVisits) {        
        for (int i = 0; i < dungeons.length; i++) {
            if (!visited[i] && fatigue >= dungeons[i][0]) {
                visited[i] = true;
                explore(fatigue - dungeons[i][1], numOfVisits);
                visited[i] = false;
            }
        }
        
        maximum = Math.max(numOfVisits, maximum);
    }
}