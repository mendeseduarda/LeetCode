# Valid Sudoku

## Problem Statement

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.

The board may be partially filled, where empty cells are filled with the character '.'.

## Example 1

**Input:**
```
[
  ["5","3",".",".","7",".",".",".","."]
  ["6",".",".","1","9","5",".",".","."]
  [".","9","8",".",".",".",".","6","."]
  ["8",".",".",".","6",".",".",".","3"]
  ["4",".",".","8",".","3",".",".","1"]
  ["7",".",".",".","2",".",".",".","6"]
  [".","6",".",".",".",".","2","8","."]
  [".",".",".","4","1","9",".",".","5"]
  [".",".",".",".","8",".",".","7","9"]
]
```
**Output:**
```
True
```

## Example 2

**Input:**
```
[
  ["8","3",".",".","7",".",".",".","."]
  ["6",".",".","1","9","5",".",".","."]
  [".","9","8",".",".",".",".","6","."]
  ["8",".",".",".","6",".",".",".","3"]
  ["4",".",".","8",".","3",".",".","1"]
  ["7",".",".",".","2",".",".",".","6"]
  [".","6",".",".",".",".","2","8","."]
  [".",".",".","4","1","9",".",".","5"]
  [".",".",".",".","8",".",".","7","9"]
]
```
**Output:**
```
False
```

## Constraints
- The board is a 9x9 2D list of strings.
- Each element is '1'-'9' or '.'.
