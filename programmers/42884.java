/*
 * 42884. 단속카메라
 */
import java.util.Arrays;

class Solution {
    public int solution(int[][] routes) {
        int cam = Integer.MIN_VALUE, numOfCams = 0;

        Arrays.sort(routes, (one, another) -> one[1] - another[1]);

        for (var route : routes) {
            if (cam < route[0]) {
                cam = route[1];
                numOfCams++;
            }
        }

        return numOfCams;
    }
}