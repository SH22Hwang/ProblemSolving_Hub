# 오늘은 피곤하니까 쉬운걸로다가

import sys
input = sys.stdin.readline

def main():
    word = input()
    n = int(input())
    
    print(word[n-1])

if __name__ == "__main__":
    main()