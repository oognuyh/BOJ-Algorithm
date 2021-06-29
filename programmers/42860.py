"""
    42860. 조이스틱
"""
def solution(name: str) -> int:
    updown_counts = [min(ord("Z") - ord(character) + 1, ord(character) - ord("A")) for character in name]
    
    cursor, count = 0, 0
    
    while True:
        count += updown_counts[cursor]
        updown_counts[cursor] = 0
        
        if sum(updown_counts) == 0: return count
        
        left, right = 1, 1
        
        while updown_counts[cursor - left] == 0:
            left += 1
            
        while updown_counts[cursor + right] == 0:
            right += 1
            
        count += left if left < right else right
        cursor += -left if left < right else right