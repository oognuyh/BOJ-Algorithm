'''
    14681. 사분면 고르기
'''
x, y = int(input()), int(input())
if x > 0: print('1' if y > 0 else '4')
else: print('2' if y > 0 else '3')