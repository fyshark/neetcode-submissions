class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character> row[] = new HashSet[9];
        HashSet<Character> col[] = new HashSet[9];
        HashSet<Character> box[] = new HashSet[9];

        for (int i = 0; i < 9; i++) {
            row[i] = new HashSet();
            col[i] = new HashSet();
            box[i] = new HashSet();
        }

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char value = board[r][c];
                int boxId = r / 3 * 3 + c / 3;

                if (value == '.') continue;
                if (row[r].contains(value) || col[c].contains(value) || box[boxId].contains(value)) {
                    return false;
                }
                row[r].add(value);
                col[c].add(value);
                box[boxId].add(value);
            }
        }
        return true;
    }
}
