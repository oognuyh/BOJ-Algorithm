"""
    14889. 스타트와 링크
"""
from itertools import combinations

N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]

# 팀 나누기
teams = list(combinations(range(N), N // 2))

# 한 팀과 상대팀으로 나누기
opposing_teams = reversed(teams[len(teams) // 2:])
teams = teams[:len(teams) // 2]

# 답에 최댓값 저장
answer = float('inf')

def get_stats(target):
    # 해당 팀의 능력치 합을 반환하는 함수
    return sum([stats[i][j] + stats[j][i] for i, j in combinations(target, 2)])

for team, opposing_team in zip(teams, opposing_teams):
    # 각 팀의 능력치 계산
    team_stats, opposing_team_stats = get_stats(team), get_stats(opposing_team)

    # 능력치 차이 계산
    diff = abs(team_stats - opposing_team_stats)

    # 능력치 차이가 답보다 작을 경우 답에 저장
    answer = diff if answer > diff else answer

    # 0일 경우 가능한 최솟값이므로 더 이상 진행하지 않음
    # 추가할 경우 1456ms -> 464ms
    if answer == 0: break

print(answer)