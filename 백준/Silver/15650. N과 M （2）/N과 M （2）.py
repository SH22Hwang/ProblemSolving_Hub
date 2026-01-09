import itertools # 이게 아닌가?
import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    nums = list(range(1, n+1))

    value_seq = itertools.combinations(nums, m)
    unique_seqs = sorted(set(value_seq))
    result = map(lambda x: ' '.join(map(str, x)), unique_seqs)

    print(*result, sep='\n')


if __name__ == "__main__":
    main()