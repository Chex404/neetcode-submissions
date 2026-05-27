class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        from collections import defaultdict

        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):

                value = board[i][j]

                if value == ".":
                    continue

                box_index = (i // 3) * 3 + (j // 3)

                if value in rows[i] or value in columns[j] or value in boxes[box_index]:
                    return False

                rows[i].add(value)
                columns[j].add(value)
                boxes[box_index].add(value)

        return True
        