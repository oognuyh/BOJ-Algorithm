
/*
 * 64064. 불량 사용자
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

class Solution {

    Set<List<String>> cases = new HashSet<>();

    List<List<String>> candidates;

    public void dfs(int index, List<String> temp) {
        if (index == candidates.size()) {
            Collections.sort(temp);
            cases.add(temp);
            return;
        }

        for (var candidate : candidates.get(index)) {
            if (temp.contains(candidate))
                continue;

            temp.add(candidate);
            dfs(index + 1, temp);
            temp.remove(candidate);
        }
    }

    public int solution(String[] user_id, String[] banned_id) {
        this.candidates = Arrays.stream(banned_id)
                .map((id) -> "^" + id.replace("*", ".") + "$")
                .map((id) -> Arrays.stream(user_id)
                        .filter((uid) -> uid.matches(id))
                        .collect(Collectors.toList()))
                .collect(Collectors.toList());

        dfs(0, new ArrayList<>());

        return cases.size();
    }
}