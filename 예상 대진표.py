import math
import time
from numpy import pi, zeros, ndarray


def solution(n, a, b):
    answer = 0

    height = math.log2(n)
    print(height)
    for i in range(1, height+1):
        a = (a + 1) / 2
        b = (b + 1) / 2
        if a == b:
            answer = i

    return answer


def main():
    n, a, b = map(int, input().split())
    start = time.process_time()
    print("answer:", solution(n, a, b))
    end = time.process_time()
    print("소요시간:", end - start)


if __name__ == "__main__":
    main()
