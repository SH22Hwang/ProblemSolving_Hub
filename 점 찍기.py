"""
시간초과
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (6866.73ms, 10.3MB)
테스트 4 〉	통과 (1815.28ms, 10.4MB)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	통과 (2509.88ms, 10.4MB)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	통과 (0.99ms, 10.1MB)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)

나눗셈을 이용하자! 포기!
"""
import time
from numpy import pi, zeros, ndarray


def solution(k, d):
    answer = 0

    ary: ndarray = zeros((d + 1, d + 1), dtype=int)

    for x in range(0, d + 1, k):
        for y in range(0, d + 1, k):
            if d >= (x ** 2 + y ** 2) ** 0.5:
                ary[x][y] = 1
                answer += 1

    c = (d + 1) ** 2 - (pi * ((d + 1) ** 2) / 4)

    for x in range(0, d + 1, k):
        for y in range(d - x, d + 1, k):
            pass

    print(ary)
    print("(d+1) ^ 2애서 원을 뺸 넓이:", c)
    print(int(((d + 1) ** 2 - c) / k ** 2))

    return answer


def main():
    k, d = map(int, input().split())
    start = time.process_time()
    print("answer:", solution(k, d))
    end = time.process_time()
    print("소요시간:", end - start)


if __name__ == "__main__":
    main()
