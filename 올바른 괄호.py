import sys
def solution():
    s = list(input())
    stack = []

    for i in s:
        try:
            if i == '(':
                stack.append('s')
            elif i == ')':
                stack.pop()
        except IndexError:
            print("False")
            return False

    print('NO' if stack else 'YES')
    return False if stack else True


if __name__ == "__main__":
    input = sys.stdin.readline
    solution()
