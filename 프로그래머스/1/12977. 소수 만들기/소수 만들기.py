def solution(nums):
    sieve = [True] * 3000
    sieve[0] = False
    sieve[1] = False
    sieve[2] = True

    for i in range(2, 56):
        if sieve[i]:
            for j in range(i + i, 3000, i):
                sieve[j] = False
                
    answer = 0
    # 중복제거하지 마라
    
    length = len(nums)
    for x in range(length-2):
        for y in range(x+1, length-1):
            for z in range(y+1, length):
                if sieve[nums[x] + nums[y] + nums[z]]:
                    answer = answer + 1
    
    return answer