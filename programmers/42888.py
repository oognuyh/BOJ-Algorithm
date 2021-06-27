"""
    42888. 오픈채팅방
"""
from collections import defaultdict
from typing import List

def solution(record: List[str]) -> List[str]:
    answer, user = [], defaultdict(str)

    for log in record:
        command, log = log.split(maxsplit = 1)

        if command == "Leave":
            uid = log

            answer.append((uid, "님이 나갔습니다."))
        else:
            uid, user_name = log.split()

            user[uid] = user_name

            if command == "Enter": 
                answer.append((uid, "님이 들어왔습니다."))

    return [user[uid] + message for uid, message in answer]