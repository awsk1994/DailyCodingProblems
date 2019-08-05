'''
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''

from collections import deque

def is_end(elem, end):
	return elem[0] == end[0] and elem[1] == end[1]

def is_not_wall(tile, matrix):
	return matrix[tile[0]][tile[1]] == False

def is_valid_tile(seen, matrix, tile):
	t0_within_bounds = (tile[0] < len(matrix) and tile[0] >= 0)
	t1_within_bounds = (tile[1] < len(matrix[0]) and tile[1] >= 0)
	return (t0_within_bounds and t1_within_bounds) and (is_not_wall(tile, matrix) and tile not in seen)	# in range, not tree and not already seen.

def get_neighbors(seen, matrix, elem):
    return [n for n in [
        (elem[0], elem[1]+1),   # top  
        (elem[0] - 1, elem[1]), # left
        (elem[0], elem[1]-1),   # bot
        (elem[0] + 1, elem[1])  # right
    ] if is_valid_tile(seen, matrix, n)]

def bfs(matrix, s, e):
    seen = set()
    q = deque()
    q.append((s, 0))
    while q:
        elem, cost = q.popleft()        
        neighbors = get_neighbors(seen, matrix, elem)
        seen.add(elem)
        for n in neighbors:
            q.append((n, cost + 1))
            if is_end(n, e):
                return cost + 1
    return None

def main():
	matrix = [[False, False, False],[False, True, False],[False, False, False]]
	start = (0,0)
	end = (2,2)
	print(bfs(matrix, start, end))

	matrix = [[False, False, False],[False, True, False],[False, True, False]]
	start = (2,0)
	end = (2,2)
	print(bfs(matrix, start, end))

if __name__ == "__main__":
	main()
