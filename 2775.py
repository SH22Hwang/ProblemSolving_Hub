# 뭉탱이로 만들어서 에러 발생한 듯. 딱 원하는 범위만 하게 고치자

import sys
input = sys.stdin.readline

import pprint

def main():
    t = int(input())


    for _ in range(t):
        k = int(input()) # k층
        n = int(input()) # n호 
        # 구할 것: k-1층의 1~n까지의 합
        countApt(k, n)
        print(apt[k][n])

    # aptt = [[1] + list(range(1, 15))]
    # for i in range(1, 15): # i: 층수, k호실까지
    #     aptt.append([0] * 15)
    #     if not aptt[i][0]:
    #         for j in range(1, 15): 
    #             aptt[i][j] += aptt[i-1][j] + aptt[i][j-1]
            
    #     aptt[i][0] = 1    

    # pprint.pprint(apt)
def countApt(k, n):
    apt.append([0] * 15)
    for f in range(1, k+1): # 1부터 k층까지
        if not apt[f][0]: # 이거 왜 넣었더라
            for r in range(1, n+1): # 1호부터 n호까지
                apt[f][r] += apt[f-1][r] + apt[f][r-1]
            
        apt[f][0] = 1


if __name__ == "__main__":
    apt = [[0] + list(range(1, 15))]
    main()