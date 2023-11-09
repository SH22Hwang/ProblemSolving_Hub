def solution(nums):
    sieve = [True] * 3000
    sieve[0] = False
    sieve[1] = False
    sieve[2] = True

    for i in range(2, 56):
        if sieve[i]:
            for j in range(i + i, 3000, i):
                sieve[j] = False

    nums = sorted(nums)

    answer = -1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    print(sorted(nums))

    return answer


if "__name__" == "__main__":
    n = int(input())
    solution(n)
