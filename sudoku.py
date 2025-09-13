
from collections import defaultdict
from typing import List

def is_valid_sudoku(board: List[List[str]]) -> bool:
	rows = defaultdict(set)
	columns = defaultdict(set)
	boxes = defaultdict(set)

	for i in range(9):
		for j in range(9):
			current = board[i][j]
			if current == ".":
				continue
			if (current in rows[i] or
				current in columns[j] or
				current in boxes[(i // 3, j // 3)]):
				return False	
			
			rows[i].add(current)
			columns[j].add(current)
			boxes[(i // 3, j // 3)].add(current)

	return True


# Exemplo de uso:
if __name__ == "__main__":
	board = [
		["5","3",".",".","7",".",".",".","."],
		["6",".",".","1","9","5",".",".","."],
		[".","9","8",".",".",".",".","6","."],
		["8",".",".",".","6",".",".",".","3"],
		["4",".",".","8",".","3",".",".","1"],
		["7",".",".",".","2",".",".",".","6"],
		[".","6",".",".",".",".","2","8","."],
		[".",".",".","4","1","9",".",".","5"],
		[".",".",".",".","8",".",".","7","9"]
	]
	print(is_valid_sudoku(board))