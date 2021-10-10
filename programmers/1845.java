/*
 * 1845. 폰켓몬
 */
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] nums) {
        int numOfUniques = Arrays.stream(nums)
            .boxed()
            .collect(Collectors.toSet())
            .size();
        
        return numOfUniques > nums.length / 2 ? nums.length / 2 : numOfUniques;
    }
}
/*
 * # Others
 *      1. Collectors.collectingAndThen()을 사용하면 collect 후 return 값을 설정할 수 있다.
 *          return Arrays.stream(nums)
 *              .boxed()
 *              .collect(Collectors.collectingAndThen(Collectors.toSet(), 
 *                              uniques -> Integer.min(uniques.size(), nums.length / 2)));
 */