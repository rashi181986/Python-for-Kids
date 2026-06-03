def find_all_paths(maze):
    n = len(maze)
    paths = []
    visited = [[False for _ in range(n)] for _ in range(n)]

    def solve(row, col, current_path):
        # Base Case: Reached the destination
        if row == n - 1 and col == n - 1:
            paths.append(current_path)
            return

        # Directions: Down, Left, Right, Up
        directions = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]

        for direction, dr, dc in directions:
            next_r, next_c = row + dr, col + dc

            # Check if the move is within bounds, not a wall (0), and not visited
            if 0 <= next_r < n and 0 <= next_c < n and \
               maze[next_r][next_c] == 1 and not visited[next_r][next_c]:
                
                visited[row][col] = True
                solve(next_r, next_c, current_path + direction)
                visited[row][col] = False  # Backtrack

    # Start solving if the entrance isn't blocked
    if maze[0][0] == 1:
        solve(0, 0, "")
    return paths

# Example Maze: 1 = Path, 0 = Wall
example_maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

result = find_all_paths(example_maze)
print(f"Total paths found: {len(result)}")
print(f"Paths: {result}")
