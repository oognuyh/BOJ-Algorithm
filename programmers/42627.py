"""
    42627. 디스크 컨트롤러
"""
from typing import List
import heapq

def solution(jobs: List[List[int]]) -> int:
    num_of_jobs, total_time, current_time = len(jobs), 0, 0

    jobs.sort(key = lambda job: job[1])
    
    while jobs:
        for i, job in enumerate(jobs):
            request_at, working_time = job
            if request_at <= current_time:
                current_time += working_time
                total_time += current_time - request_at

                jobs.pop(i)
                break
            
            current_time += 1 if not jobs[i + 1:] else 0

    return total_time // num_of_jobs