"""
    200. Number of Islands
"""
WATER = '0'
LAND = '1'

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def move(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == WATER:
                return 

            grid[r][c] = WATER

            move(r + 1, c)
            move(r - 1, c)
            move(r, c + 1)
            move(r, c - 1)       
        
        count = 0
        if not grid: return count
        
        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == LAND:
                    move(row, col)
                    count += 1
                else:
                    pass

        return count

"""
    - 136 ms 15.3 MB

    # Others
        1. ??? - 116 ms 15.4 MB
            m = len(grid)
            n = len(grid[0])

            water = 0
            land = 1

            for row in grid:
                row[:] = [land if c != '0' else water for c in row]

            def findRuns(row):
                pc = water
                for j, c in enumerate(row):
                    if c != pc:
                        if c != water:
                            b = j
                        else:
                            yield b, j
                    pc = c

                if pc != water:
                    yield b, len(row)

            islands_count = 0
            prev_row = [water] * n
            id_counter = 1
            for row in grid:
                row = row[:]
                for b, e in findRuns(row):
                    prev_islands = set(prev_row[b:e]) - set([water])
                    if len(prev_islands) == 0:
                        # A new island discovered.
                        islands_count += 1
                        id = id_counter
                        id_counter += 1
                    elif len(prev_islands) == 1:
                        # Just continue a known island.
                        for id in prev_islands:
                            break
                    else:
                        # Join what was previously thought to be several islands.
                        islands_count -= len(prev_islands) - 1
                        for id in prev_islands:
                            break

                        row[:] = [id if c in prev_islands else c for c in row]
                        prev_row[:] = [id if c in prev_islands else c for c in prev_row]

                    row[b:e] = [id] * (e - b)

                prev_row = row

            return islands_count
"""