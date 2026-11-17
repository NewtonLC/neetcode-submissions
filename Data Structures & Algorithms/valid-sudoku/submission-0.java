class Solution {
    public boolean isValidSudoku(char[][] board) {
        /*
        in:  int[][], contains digits 1-9, periods for empty squares
        out: true/false, is the sudoku board valid?
        con:
        - Each row must contain the digits 1-9 without duplicates.
        - Each column must contain the digits 1-9 without duplicates.
        - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
        - A board does not need to be full or solvable to be valid.
        edge/ex:
        - empty board --> true
        
        Plan:
        Brute Force:
        1. Check every row for duplicates
        2. Check every col for duplicates
        3. Check every 3x3 square for duplicates
        Time: 243 checks. O(n^2), Space: O(1)

        Set() --> sets only contain 1 of each element
        - put every row/col/3x3 into a set
        - If the number of digits > set.length, it has duplicates, return false.
        - Still brute forcing

        Map? & Coordinates Tracking
        - 1 at (0,0) and (7,4)
        - 2 at (0,1), (5,4), and (6,6)
        and so on

        - Row --> For digits 1-9, do any of the first coordinate overlap? --> yes --> return false
        - Col --> For digits 1-9, do any of the first coordinate overlap? --> yes --> return false
        - 3x3 --> (0,0) + 2, (0,3) + 2, (0,6) + 2, 
        */

        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<String, Set<Character>> squares = new HashMap<>();

        for (int r = 0;r < 9;r++){
            for (int c = 0;c < 9;c++){
                if (board[r][c] == '.'){
                    continue;
                }

                String squareKey = (r/3) + "," + (c/3);

                //Run all 3 checks (rows, cols, grids)
                // 1. Create the rows, columns, and squares if they're absent.
                //    AND it also checks if they contain board[r][c]. Return false if duplicate
                if (rows.computeIfAbsent(r, k -> new HashSet<>()).contains(board[r][c]) ||
                    cols.computeIfAbsent(c, k -> new HashSet<>()).contains(board[r][c]) ||
                    squares.computeIfAbsent(squareKey, k -> new HashSet<>()).contains(board[r][c])){
                        return false;
                }
                
                // 2. Add board[r][c] to the rows, cols, and squares.
                rows.get(r).add(board[r][c]);
                cols.get(c).add(board[r][c]);
                squares.get(squareKey).add(board[r][c]);
            }
        }

        return true;
    }
}
