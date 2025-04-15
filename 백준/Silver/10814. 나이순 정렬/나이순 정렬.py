import sys
input = sys.stdin.readline

def main():
    line = int(input())
    students = [input().split() + [x] for x in range(line)]
    
    students.sort(key=lambda x: (int(x[0]), x[2]))  # 나이순 + 입력 순
    
    # print(students)
    for x in range(line):
        print(f"{students[x][0]} {students[x][1]}")

if __name__ == "__main__":
    main()