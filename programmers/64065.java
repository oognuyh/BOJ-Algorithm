/*
 * 64065. 튜플
 */
import java.util.Comparator;
import java.util.stream.Stream;

class Solution {
    public int[] solution(String s) {        
        return Stream.of(s.split("[{.+}],?"))
            .filter(str -> !str.isEmpty())
            .map(str -> str.split(","))
            .sorted(Comparator.comparing(array -> array.length))
            .flatMap(Stream::of)
            .distinct()
            .mapToInt(Integer::parseInt)
            .toArray();
    }
}