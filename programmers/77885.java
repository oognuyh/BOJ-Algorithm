/*
 * 77885. 2개 이하로 다른 비트
 */
import java.util.Arrays;

class Solution {
    public long[] solution(long[] numbers) {
        return Arrays.stream(numbers)
            .map(number -> {
                if (number % 2 == 0) {
                    return number + 1;
                } else {
                    String binary = Long.toBinaryString(number);
                    int lastZeroIndex = binary.lastIndexOf('0');
                    return Long.parseLong(
                        lastZeroIndex < 0 ?
                            "10" + binary.substring(1).replace("0", "1") :
                            binary.substring(0, lastZeroIndex) + "10" + binary.substring(lastZeroIndex + 2)
                    , 2);
                }
            })
            .toArray();
    }
}
/*
 * # Others
 *      1. 비트 이동/논리 연산자
 *          return Arrays.stream(numbers)
 *              .map(number -> (number + 1) + (((number + 1) ^ number) >>> 2))
 *              .toArray();
 */