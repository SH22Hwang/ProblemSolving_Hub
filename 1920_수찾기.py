# left는 nums1의 수 보다 작은 게 nums2에 있으면 0으로 나옴 그것이 이진탐색이니까... 음
# right는 nums1의 수 보다 큰 게 nums2에 있으면 len1으로 나옴 그것이 이진탐색이니까... 음

# 이진탐색 left, right 2번 해서 풀었는데, 이진탐색 한 번만 써서 간소화해보자
# set을 이용하여 풀어보자

from bisect import bisect_left, bisect_right

def main():
    # 이진탐색
    len1 = int(input())
    nums1 = sorted(list(map(int, input().split())))

    len2 = int(input())
    nums2 = list(map(int, input().split()))
    
    # print(nums1, nums2)
    
    for n in nums2:
        # print(n)
        # print("left: ", bisect_left(nums1, n))
        right = bisect_right(nums1, n)
        left = bisect_left(nums1, n)
        print(f'n: {n}, right: {right}, left: {left}', end=' ')
        if (left == right):
            print(0)
        else:
            print(1)
        # print("right: ", bisect_right(nums1, n))
    

if __name__ == "__main__":
    main()


# 딕셔너리리
# def main():
    # _ = int(input())
    # nums1_dict = {num: 1 for num in map(int, input().split())}

    # _ = int(input())
    # nums2 = list(map(int, input().split()))

    # print(nums1_dict)

    # for i in nums2:
    #     try:
    #         print(nums1_dict[i])
    #     except:
    #         print(0)


# 시간 초과될 듯

    # _ = int(input())
    # nums1 = list(map(int, input().split()))

    # _ = int(input())
    # nums2 = list(map(int, input().split()))

    # pluslist = [False] * (2 ** 31 - 1)
    # minuslist = [False] * (2 ** 31 - 1)

    # for i in nums1:
    #     if i < 0:
    #         minuslist[i] = True
    #     else:
    #         pluslist[i] = True
    
    # for i in nums2:
    #     if i < 0:
    #         print(int(minuslist[i]))
    #     else:
    #         print(int(pluslist[i]))