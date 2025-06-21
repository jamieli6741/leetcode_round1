# https://kamacoder.com/problempage.php?pid=1171
# ACM mode
import sys
from io import StringIO
from collections import deque

offsets = [[0,1],[1,0],[0,-1],[-1,0]]
def dfs(grid, visited, x, y):
    for dx,dy in offsets:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
            continue
        if grid[nx][ny] == 1 and visited[nx][ny] == False:
            visited[nx][ny] = True
            dfs(grid, visited, nx, ny)

def bfs(grid, visited, x, y):
    queue = deque([(x,y)])
    visited[x][y] = True
    while len(queue) > 0:
        x,y = queue.popleft()
        for dx,dy in offsets:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                continue
            if grid[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))


def main():
    n, m = map(int,input().split())
    grid = []
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    visited = [[False]*m for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and visited[i][j] == False:
                result += 1
                # visited[i][j] = True
                # dfs(grid, visited, i, j)
                bfs(grid, visited, i, j)

    print(result)

if __name__ == '__main__':
    test_input = '''4 5
    1 1 0 0 0
    1 1 0 0 0
    0 0 1 0 0
    0 0 0 1 1
    '''

    sys.stdin = StringIO(test_input)
    main()