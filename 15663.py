# n과 m 백트래킹을 써라?
# 백트래킹이란? 상태공간을 트리로 만들어라? 트리를 어케만듦? 배열로 구현해야하나 아니면 연결리스트?

import itertools
import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))

    # print(f'n: {n}, m: {m}')
    # print("nums:", nums)

    # sequence_tree = [] 
    # idx_seq = itertools.permutations(range(n), m)
    value_seq = itertools.permutations(nums, m)
    unique_seqs = sorted(set(value_seq))
    result = map(lambda x: ' '.join(map(str, x)), unique_seqs)

    # print(sorted(set(value_seq)))
    # print(list(result))
    print(*result, sep='\n')


if __name__ == "__main__":
    main()