import java.util.HashSet;
import java.util.Set;

public class validsudoku {
    public static void main(String[] args) {
        char [] [] board = {{'5','3','.','.','7','.','.','.','.'}
                           ,{'6','.','.','1','9','5','.','.','.'}
                        ,{'.','9','8','.','.','.','.','6','.'}
                        ,{'8','.','.','.','6','.','.','.','3'}
                        ,{'4','.','.','8','.','3','.','.','1'}
                        ,{'7','.','.','.','2','.','.','.','6'}
                        ,{'.','6','.','.','.','.','2','8','.'}
                        ,{'.','.','.','4','1','9','.','.','5'}
                        ,{'.','.','.','.','8','.','.','7','9'}};

                        
        isValidSudoku(board);
    }

    public static boolean isValidSudoku(char[][] board) {
        Set<Character> rows = new HashSet<>();
        Set<Character> columns = new HashSet<>();

        Set<Character> sq1 = new HashSet<>();
        Set<Character> sq2 = new HashSet<>();
        Set<Character> sq3 = new HashSet<>();

        for(int i = 0; i < 9; i++){
            for(int x = 0; x < 9; x++){
                char currRow = board[i][x];
                char currColumn = board[x][i];
            
                if(rows.contains(currRow) || columns.contains(currColumn)){
                    return false;
                }

                if(currRow != '.'){
                    rows.add(currRow);
                }

                if(currColumn != '.'){
                    columns.add(currColumn);
                }
            }

            rows = new HashSet<>();
            columns = new HashSet<>();
        }

        for(int i = 0; i < 9; i += 3){
            for(int x = 0; x < 27; x++){

                char curr = board[x % 9][(x/9) + i];
                if(curr != '.'){

                    if(x % 9 < 3){
                        if(sq1.contains(curr)){
                            return false;
                        }
                        else{
                            sq1.add(curr);
                        }
                    }

                    else if(x % 9 < 6){
                        if(sq2.contains(curr)){
                            return false;
                        }
                        else{
                            sq2.add(curr);
                        }
                    }

                    else{
                        if(sq3.contains(curr)){
                            return false;
                        }
                        else{
                            sq3.add(curr);
                        }
                    }
                }
            }
            
            sq1 = new HashSet<>();
            sq2 = new HashSet<>();
            sq3 = new HashSet<>();
        }

        return true;
    }
}
