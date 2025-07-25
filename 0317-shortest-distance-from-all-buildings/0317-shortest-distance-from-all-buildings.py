class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        from collections import deque
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        total_dist = [[0] * n for _ in range(m)]
        reach = [[0] * n for _ in range(m)]
        num_buildings = 0

        # BFS from each building
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_buildings += 1
                    visited = [[False] * n for _ in range(m)]
                    queue = deque([(i, j, 0)])  # (x, y, distance)

                    while queue:
                        x, y, dist = queue.popleft()
                        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                                if grid[nx][ny] == 0:
                                    visited[nx][ny] = True
                                    total_dist[nx][ny] += dist + 1
                                    reach[nx][ny] += 1
                                    queue.append((nx, ny, dist + 1))

        # Find the minimum total distance
        min_dist = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[i][j] == num_buildings:
                    min_dist = min(min_dist, total_dist[i][j])

        return min_dist if min_dist != float('inf') else -1
