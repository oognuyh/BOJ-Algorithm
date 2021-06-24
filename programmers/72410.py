"""
    72410. 신규 아이디 추천
"""
import re

def solution(new_id):
    converted_id = new_id.lower() 
    converted_id = re.sub("[^a-z0-9-_\.]", "", converted_id) 
    converted_id = re.sub("[\.]+", ".", converted_id) 
    converted_id = converted_id.lstrip(".").rstrip(".") 
    
    if not converted_id:
        converted_id += "a"
    
    if len(converted_id) >= 16: 
        converted_id = converted_id[:15].rstrip(".")
    
    if len(converted_id) <= 2: 
        while len(converted_id) < 3:
            converted_id += converted_id[-1]

    return converted_id