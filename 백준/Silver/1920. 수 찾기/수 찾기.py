from bisect import bisect_left, bisect_right

def main():
    # 이진탐색
    len1 = int(input())
    nums1 = sorted(list(map(int, input().split())))

    len2 = int(input())
    nums2 = list(map(int, input().split()))
    
    for n in nums2:
        right = bisect_right(nums1, n)
        left = bisect_left(nums1, n)
        if (left == right):
            print(0)
        else:
            print(1)
    

if __name__ == "__main__":
    main()