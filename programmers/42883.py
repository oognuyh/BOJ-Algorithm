"""
    42883. 큰 수 만들기
"""
def solution(number: str, k: int) -> str: 
    number, answer, left = list(number), [], 0
        
    for right in range(k + 1, len(number) + 1):
        max_number, max_number_index = -1, 0
        
        for i, n in enumerate(number[left:right], start = left):
            if int(max_number) < int(n):
                max_number, max_number_index = n, i
                if max_number == "9": break
                
        answer.append(max_number)
        left = max_number_index + 1
        
    return ''.join(answer)

"""
    # Others
        1. stack
            def solution(number, k):
                st = []
                
                for i in range(len(number)):
                    while st and k > 0 and st[-1] < number[i]:
                        st.pop()
                        k -= 1
                    st.append(number[i])

                return ''.join(st[:len(st) - k])
"""