# 5 ** 20개
# 칸토어 수열은 대칭이다..!

import time

def solution(n, l, r):
    n, l, r = int(n), int(l), int(r)
    cantor = ["1", "11011"]
    answer = 0

    for i in range(2, n + 1):
        prev = cantor[i - 1] * 2
        cur = ''.join([prev, '00000' * 5 ** (i - 2), prev])
        cantor.append(cur)
        print(i, cur)

    target = cantor[n][l - 1:r]
    answer = target.count('1')
    # answer = sum(map(int, cantor[n][l - 1:r]))
    return answer


def main():
    n, l, r = input().split()
    start = time.process_time()
    print(solution(n, l, r))
    end = time.process_time()
    print(end - start)


if __name__ == "__main__":
    main()
