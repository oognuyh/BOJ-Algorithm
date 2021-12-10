/*
 * 77486. 다단계 칫솔 판매
 */
import java.util.Arrays;
import java.util.Map;
import java.util.stream.Collectors;

class Solution {
    class Salesman {
        String name;
        int profit = 0; 
        Salesman supervisor;

        public Salesman(String name) {
            this.name = name;
        }

        void distribute(int profit) {
            int fee = profit / 10;
            this.profit += profit - fee;

            if (this.supervisor != null && fee > 0) 
                this.supervisor.distribute(fee);
        }
    }

    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        Map<String, Salesman> salesmans = Arrays.stream(enroll)
            .collect(Collectors.toMap(name -> name, Salesman::new));

        for (int i = 0; i < referral.length; i++) {
            if (referral[i].equals("-")) continue;

            salesmans.get(enroll[i]).supervisor = salesmans.get(referral[i]);
        }

        for (int i = 0; i < seller.length; i++) {
            salesmans.get(seller[i]).distribute(amount[i] * 100);
        }

        return Arrays.stream(enroll)
            .mapToInt(name -> salesmans.get(name).profit)
            .toArray();
    }
}