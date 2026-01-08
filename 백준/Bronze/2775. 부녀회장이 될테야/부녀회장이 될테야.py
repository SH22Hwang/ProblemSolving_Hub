# 뭉탱이로 만들어서 에러 발생한 듯. 딱 원하는 범위만 하게 고치자

import sys
input = sys.stdin.readline

# import pprint

def main():
    t = int(input())


    for _ in range(t):
        k = int(input()) # k층
        n = int(input()) # n호 
        # 구할 것: k-1층의 1~n까지의 합
        countApt(k, n)
        print(apt[k][n])

    # pprint.pprint(apt)


def countApt(k, n):
    for f in range(1, k+1): # 1부터 k층까지
        apt.append([0] * 15)
        for r in range(1, n+1): # 1호부터 n호까지
            if not apt[f][r]:
                apt[f][r] += apt[f-1][r] + apt[f][r-1]



if __name__ == "__main__":
    apt = [list(range(15))]
    main()