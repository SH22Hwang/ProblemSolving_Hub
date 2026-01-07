import sys
input = sys.stdin.readline


def main():
    n = int(input())
    coordinates = []

    for _ in range(n):
        x, y = map(int, input().split())
        coordinates.append((x, y))

    print(coordinates)


if __name__ == "__main__":
    main()