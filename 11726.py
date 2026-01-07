# 음 잘 모르겠으니 일단 넘어가고 당장 급한 정렬을 풀어보자

# 2xN 타일링
# 1. 나무토막이 늘어날때마다 숫자 늘리기?
# 2. 세로는 0 가로는 1 <- 채택

import sys
input = sys.stdin.readline


def main():
    n = int(input())

    mat0 = []

    mat11 = [[0],
             [0]]
    mat1 = [mat11]

    mat21 = [[0, 0],
             [0, 0]]
    mat22 = [[1, 1],
             [1, 1]]
    mat2 = [mat21, mat22]

    # mat31 = [[0, 0, 0],
    #          [0, 0, 0]]
    # mat32 = [[1, 1, 0],
    #          [1, 1, 0]]
    # mat33 = [[1, 0, 0],
    #          [1, 0, 0]]
    # mat3 = [mat31, mat32, mat33]

    dp_matrix = [mat0, mat1, mat2]

    if n >= 3:
        for x in range(3, n+1):
            # dp_matrix[x] = dp_matrix[x-1] + dp_matrix[x-2]
            # mat_x 계산법
            # dp 국룰: dp_matrix[x-1]에서 하나, dp_matrix[x-2]에서 하나씩 가져옴
                # x-1, x-2에서 가져오는 거 맞나?
                # 3은 2, 1에서 가져오는 거 맞음
                # 4? 1, 3 / 2, 2에서 다 가져와야함
                # 5? 2, 3 / 1, 4에서 다...
                # 그럼 1부터 x-1까지 다 돌아야겠네 

            # 1. a: dp_matrix[0], b: dp_matrix[x-1] 가져옴
            # 2. 둘이 concat
            # 3. mat_x에서 중복 검사하고 mat_x에 추가
            # 4. a의 인덱스가 x-1, b의 인덱스가 1이 될 때까지 반복

            dp_matrix.append([]) # x 크기의 타일 경우의 수가 들어갈 자리
            mat_x = [] # x 크기의 타일 경우의 수

            idx_a = 1
            idx_b = x-1
            while(idx_a < x and idx_b >= 0):
                mat_a = dp_matrix[idx_a] # n: 3일 때 1 크기의 타일 모든 경우의 수
                mat_b = dp_matrix[idx_b] # n: 3일 때 2 크기의 타일 모든 경우의 수
                print(mat_a)
                print(mat_b)
                tmp = mat_concat(mat_a, mat_b) # 이게 아니네
                                               # 경우의 수에서 또 하나씩만 뽑아야 함 개같은거
                
                isDuplicate = False
                for y in mat_x: # 중복검사 
                    if tmp == y:
                        isDuplicate = True
                        break
                
                if not isDuplicate:
                    mat_x.append(tmp)

                idx_a += 1
                idx_b -+ 1

                
            dp_matrix[x].append(mat_x)

    # print(len(dp_matrix[n-1]))

    for i, m in enumerate(dp_matrix):
        print(f"타일 {i}의 경우의 수: {len(m)}")
        print(m)


def mat_concat(m1, m2): # 나중에 연산자 오버로딩으로 바꿔보기
    temp1 = m1[0] + m2[0]
    temp2 = m1[1] + m2[1]
    return [temp1, temp2]


if __name__ == "__main__":
    main()