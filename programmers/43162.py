"""
    43162. 네트워크
"""
def solution(n, computers):
    def connect(i, j):
        for k in range(n):
            if computers[i][k]:                
                computers[i][k] = 0
                connect(k, i)

    num_of_networks = 0

    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                connect(i, j)
                num_of_networks += 1

    return num_of_networks

"""
    # Others
        1. 
            def solution(n, computers):
                temp = list(range(n))

                for i in range(n):
                    for j in range(n):
                        if computers[i][j]:
                            for k in range(n):
                                if temp[k] == temp[i]:
                                    temp[k] = temp[j]

                return len(set(temp))
"""

