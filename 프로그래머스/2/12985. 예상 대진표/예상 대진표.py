import math

def solution(n, a, b):
    answer = 0

    height = int(math.log2(n))
    for i in range(1, height+1):
        a = (a + 1) // 2
        b = (b + 1) // 2
        # print(f"시도 {i}: {a}, {b}")
        if a == b:
            answer = i
            break

    return answer
