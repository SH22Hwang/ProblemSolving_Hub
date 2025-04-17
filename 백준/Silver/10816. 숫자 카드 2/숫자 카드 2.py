import sys
input = sys.stdin.readline

from bisect import bisect_left, bisect_right

def main():
    _ = input()
    nums1 = sorted(list(map(int, input().split())))
    _ = input()
    nums2 = list(map(int, input().split()))

    for x in nums2:
        right = bisect_right(nums1, x)
        left = bisect_left(nums1, x)
        print(abs(left - right), end=' ')

if __name__ == "__main__":
    main()