import sys
input = sys.stdin.readline


def main():
    length = int(input())
    src = input()

    # abc = 그냥 아스키코드로 받는 게 빠를 듯 ord()
    abc = lambda x: ord(x) - 96

    rsquare = list(31 ** i for i in range(length))
    
    hash = 0
    for x in range(length):
        hash += abc(src[x]) * rsquare[x]

    print(hash % 1234567891)
    # print(hash)
    # print(rsquare)
    # print(length, src)

if __name__ == "__main__":
    main()