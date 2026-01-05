import sys
from collections import Counter

input = sys.stdin.readline

def main():
    input()  # N
    cnt = Counter(map(int, input().split()))
    input()  # M
    queries = map(int, input().split())

    result = [str(cnt[q]) for q in queries]
    sys.stdout.write(" ".join(result))

if __name__ == "__main__":
    main()
