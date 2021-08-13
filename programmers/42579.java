/*
 * 42579. 베스트앨범
 */
import java.util.Comparator;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Solution {
    class Music implements Comparable<Music> {
        int no;
        String genre;
        int play;
        
        Music(int no, String genre, int play) {
            this.no = no;
            this.genre = genre;
            this.play = play;
        }
        
        @Override
        public int compareTo(Music another) {
            return this.play == another.play ? this.no - another.no : another.play - this.play;
        }
    }
    
    public int[] solution(String[] genres, int[] plays) {
        return IntStream
            .range(0, genres.length)
            .mapToObj(no -> new Music(no, genres[no], plays[no]))
            .collect(Collectors.groupingBy(music -> music.genre))
            .values().stream()
            .sorted(Comparator.comparing(musics -> -musics.stream()
                                         .mapToInt(music -> music.play)
                                         .sum()))
            .flatMap(musics -> musics.stream()
                    .sorted()
                    .limit(2))
            .mapToInt(music -> music.no)
            .toArray();
    }
}