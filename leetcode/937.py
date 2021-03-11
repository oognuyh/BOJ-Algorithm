"""
    937. Reorder Data in Log Files
"""
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        
        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        letter_logs = sorted(letter_logs, key = lambda log: (log.split()[1:], log.split()[0]))
        
        return letter_logs + digit_logs

"""
    - 40 ms 14.4 MB

    # Others 
        1. split(seq, maxsplit) - 24 ms 14.5 MB
            letter_logs, digit_logs = [], []
        
            for log in logs:
                if log.split(" ", 1)[1][0].isdigit():
                    digit_logs.append(log)
                else:
                    letter_logs.append(log)                
            
            letter_logs.sort(key = lambda log: (log.split(" ", 1)[1], log.split(" ", 1)[0]))
            
        2. sort - 36 ms 14.4 MB
            letter_logs.sort(key = lambda log: (log.split()[1:], log.split()[0]))

    # Tips
        1. log.split(" ", 1) means to only at most one time, from left to right, upon encountering a white-space character, split the string into two strings and store the two strings in a list
        2. sort() is faster than sorted()
"""