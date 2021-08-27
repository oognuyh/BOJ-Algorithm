"""
    1844. 게임 맵 최단거리
"""
from typing import List
from collections import deque

def solution(maps: List[List[int]]) -> int:
    def is_destination(x: int, y: int) -> bool:
        return (x, y) == (width - 1, height - 1)
    
    def is_valid(x: int, y: int) -> bool:
        return -1 < x < width and -1 < y < height and maps[y][x] 
    
    width, height = len(maps[0]), len(maps)
    dq = deque([(0, 0, 1)])
    
    maps[0][0] = 0
    
    while dq:
        x, y, count = dq.popleft()        
        if is_destination(x, y): return count
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if is_valid(x + dx, y + dy):
                maps[y + dy][x + dx] = 0
                dq.append([x + dx, y + dy, count + 1])
                
    return -1