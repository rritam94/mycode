import java.util.Arrays;
import java.util.Comparator;

public class mergeintervals {
    public static void main(String[] args) {
        printMatrix(merge(new int [][] {{1,4},{0,2}, {3,5}}));
    }

    public static int[][] merge(int[][] intervals) {
        int [][] m = new int[intervals.length][2];
        Arrays.sort(intervals, Comparator.comparingInt(row -> row[0]));
        // return intervals;
        int count = 0;
      
        for(int i = 0; i < intervals.length; i++){
            if((i < intervals.length - 1) && (intervals[i][1] >= intervals[i + 1][0])){
                m[i][0] = intervals[i][0];
                m[i][1] = Math.max(intervals[i][1], intervals[i + 1][1]);
                count++;
                // i = i + 1;
            }
            
            else{
                m[i][0] = intervals[i][0];
                m[i][1] = intervals[i][1];
                count++;
            }
        }
    
        int ret [][] = new int[count][2];
        int iterator = 0;

        for(int i = 0; i < m.length; i++){
            if(m[i][0] != 0 || m[i][1] != 0){
                ret[iterator][0] = m[i][0];
                ret[iterator][1] = m[i][1];
                iterator++;
            }
        }

        return ret;
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int element : row) {
                System.out.print(element + " ");
            }
            System.out.println();
        }
    }
}
