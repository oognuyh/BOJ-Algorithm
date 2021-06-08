"""
    42586. 기능개발
"""
from itertools import starmap
from math import ceil 
from collections import deque

def solution(progresses, speeds):
    times = deque(starmap(lambda progress, speed: ceil((100 - progress) / speed), zip(progresses, speeds)))
    result, dq = [], deque()

    while times:
        time = times.popleft()

        if dq and (max(dq) < time):
            result.append(len(dq))
            dq =  deque([time])
        else:
            dq.append(time)

    if dq:
        result.append(len(dq))

    return result
    
"""
    # Others
        1. for, ceil -> -((p - 100) // s)
            def solution(progresses, speeds):
                q = []
                
                for p, s in zip(progresses, speeds):
                    if not len(q) or q[-1][0] < -((p - 100) // s):
                        q.append([-((p - 100) // s), 1])
                    else:
                        q[-1][1] += 1
                
                return list(map(lambda _q: _q[1], q))
"""