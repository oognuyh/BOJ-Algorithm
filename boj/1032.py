"""
    1032. 명령 프롬프트
"""
N = int(input())
cmd = list(input())

for i in range(N - 1):
    other = list(input())
    for j in range(len(cmd)):
        if cmd[j] != other[j]:
            cmd[j] = '?'
            
print(''.join(cmd))


    
