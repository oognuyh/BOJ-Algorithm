/*
 * 1835. 단체사진 찍기
 */
class Solution {
    String[] data;
    String friends = "ACFJMNRT";
    int numOfConditions = 0;

    public int solution(int n, String[] data) {
        this.data = data;

        getValidConditions("");

        return numOfConditions;
    }

    boolean isValid(String condition) {
        for (int i = 0; i < data.length; i++) {
            char A = data[i].charAt(0);
            char B = data[i].charAt(2);
            char operation = data[i].charAt(3);
            int diff = data[i].charAt(4) - '0' + 1;
            int conditionDiff = Math.abs(condition.indexOf(A) - condition.indexOf(B));

            if (operation == '=') {
                if (conditionDiff != diff) return false;
            } else if (operation == '>') {
                if (conditionDiff <= diff) return false;
            } else {
                if (conditionDiff >= diff) return false;
            }
        }
        return true;
    }

    void getValidConditions(String condition) {
        if (condition.length() == friends.length()) {
            if (isValid(condition)) {
                numOfConditions++;
            }
        } else {
            for (int i = 0; i < friends.length(); i++) {
                if (condition.indexOf(friends.charAt(i)) < 0) {
                    getValidConditions(condition + friends.charAt(i));
                }
            }
        }
    }
}