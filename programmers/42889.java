/*
 * 42889. 실패율
 */
import java.util.Arrays;
import java.util.Comparator;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Solution {
    class Stage {
        int no;
        int numOfFailureUsers;
        int numOfUsers;

        int getNo() { return no; }
        double getFailureRate() { return (double) numOfFailureUsers / numOfUsers; }
    }

    public int[] solution(int N, int[] stages) {
        int[] numOfUsers = { stages.length };
        Map<Integer, Long> counter = Arrays.stream(stages)
            .boxed()
            .collect(Collectors.groupingBy(stage -> stage, Collectors.counting()));

        return IntStream
            .concat(
                Arrays.stream(stages)
                    .distinct()
                    .sorted()
                    .filter(stageNo -> stageNo != N + 1)
                    .mapToObj(stageNo -> {
                        Stage stage = new Stage();

                        stage.no = stageNo;
                        stage.numOfFailureUsers = counter.get(stage.no).intValue();
                        stage.numOfUsers = numOfUsers[0];
                        numOfUsers[0] -= stage.numOfFailureUsers;

                        return stage;
                    })
                    .sorted(Comparator.comparing(Stage::getFailureRate).reversed()
                        .thenComparing(Stage::getNo))
                    .mapToInt(Stage::getNo), 
                IntStream.rangeClosed(1, N)
                    .filter(stage -> !counter.containsKey(stage)))
            .toArray();
    }
}