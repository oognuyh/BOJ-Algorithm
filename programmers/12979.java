/*
 * 12979. 기지국 설치
 */
class Solution {

    public int solution(int n, int[] stations, int w) {
        int range = 2 * w + 1;
        int numOfAdded = stations[0] - w > 1 ? (stations[0] - w - 2) / range + 1 : 0;
        int previous = stations[0] + w;

        for (int i = 1; i < stations.length; i++) {
            if (previous + 1 < stations[i] - w) {
                numOfAdded += (stations[i] - w - previous - 2) / range + 1;
            }
            previous = stations[i] + w;
        }

        if (previous < n) {
            numOfAdded += (n - previous - 1) / range + 1;
        }

        return numOfAdded;
    }
}