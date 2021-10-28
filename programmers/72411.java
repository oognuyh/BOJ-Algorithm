/*
 * 72411. 메뉴 리뉴얼
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Solution {    
    public String[] solution(String[] orders, int[] course) {
        Set<Integer> courses = Arrays.stream(course)
            .boxed()
            .collect(Collectors.toSet());

        return Arrays.stream(orders)
            .map(order -> Arrays.stream(order.split(""))
                 .sorted()
                 .toArray(String[]::new))
            .flatMap(order -> combine(order, courses))
            .collect(Collectors.groupingBy(_course -> _course.length(), 
                     Collectors.groupingBy(_course -> _course, Collectors.counting())))
            .entrySet()
            .stream()
            .flatMap(entry -> {
                long maximum = Collections.max(entry.getValue().values());

                return entry.getValue().entrySet().stream()
                    .filter(e -> e.getValue() > 1 && e.getValue() == maximum)
                    .map(e -> e.getKey());
            })
            .sorted()
            .toArray(String[]::new);
    }

    public Stream<String> combine(String[] order, Set<Integer> courses) {
        List<String> combination = new ArrayList<>();

        for (int i = 1; i < 1 << order.length; i++) {
            if (courses.contains(Integer.bitCount(i))) {
                StringBuilder sb = new StringBuilder();

                for (int j = 0; j < order.length; j++) {
                    if (((1 << j) & i) > 0) {
                        sb.append(order[j]);
                    }
                }
                combination.add(sb.toString());
            }
        }

        return combination.stream();
    }
}