
from typing import List

def is_valid_sudoku(board: List[List[str]]) -> bool:
	"""
	Recebe um tabuleiro 9x9 de Sudoku como lista de listas de strings.
	Retorna True se o tabuleiro for válido, False caso contrário.
	"""
	# ... implementação será feita aqui ...
	pass

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