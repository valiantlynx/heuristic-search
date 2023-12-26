from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Tuple

app = FastAPI()

# Allow CORS for your frontend (replace '*' with your frontend's URL)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define maze dimensions
num_rows = 10
num_cols = 10

# Sample maze (0 represents open path, 1 represents a wall)
maze = [
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
]

# Implement Breadth-First Search (BFS) algorithm
def bfs_search(start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
    queue = [(start, [])]
    visited = set()

    while queue:
        current, path = queue.pop(0)
        row, col = current

        if current == end:
            return path + [current]

        if current not in visited and maze[row][col] == 0:
            visited.add(current)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dr, col + dc
                if (
                    0 <= new_row < num_rows
                    and 0 <= new_col < num_cols
                    and (new_row, new_col) not in visited
                ):
                    queue.append(((new_row, new_col), path + [current]))

    # If BFS didn't find a path, return an empty list to indicate no path found
    return []


@app.get("/api/path")
def get_path():
    # Define the starting and ending points (modify as needed)
    start = (0, 0)
    end = (num_rows - 1, num_cols - 1)

    # Find the path using BFS
    path = bfs_search(start, end)

    # Check if a path was found
    if not path:
        return {"message": "No path found."}
    else:
        return {"path": path}
