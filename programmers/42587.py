"""
    42587. 프린터
"""
from collections import deque

def solution(priorities, location):
    documents = deque([(i, priority) for i, priority in enumerate(priorities)])
    count = 0
    
    while priorities:
        document = documents.popleft() 
        
        if documents and document[1] < max(documents, key = lambda document: document[1])[1]:
            documents.append(document)
        else:
            count += 1

            if document[0] == location:
                break
            
    return count
    
"""
    # Others
        1. any()
            def solution(priorities, location):
                queue = [(i, p) for i, p in enumerate(priorities)]
                answer = 0

                while True:
                    cur = queue.pop(0)
                    if any(cur[1] < q[1] for q in queue):
                        queue.append(cur)
                    else:
                        answer += 1
                        if cur[0] == location:
                            return answer
"""