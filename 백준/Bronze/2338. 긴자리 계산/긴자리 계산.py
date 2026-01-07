# 아마 C언어에서 문자열 이용해서 carry 넣고 계산하는 문제인 듯
# 그래서 브론즈 5인듯

import sys
input = sys.stdin.readline


def main():
    a = int(input())
    b = int(input())

    print(f"{a+b}\n{a-b}\n{a*b}")

if __name__ == "__main__":
    main()