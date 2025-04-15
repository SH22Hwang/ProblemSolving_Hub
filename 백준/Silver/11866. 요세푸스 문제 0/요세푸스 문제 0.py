# 옛날에는 C언어로 연결리스트 만들어서 품
# 이번에는 파이썬으로 큐를 갖고와서 풀어보자

import queue

def main():
    
    n, k = map(int, input().split())
    q = queue.Queue()

    for i in range(1, n + 1):
        q.put(i)

    # print(q.queue, q.qsize())

    print('<', end='')
    while not q.empty():
        for i in range(k-1):
            q.put(q.get())
        
        print(q.get(), end='')
        if not q.empty():
            print(", ", end='')
        else:
            print('>')
            break
    

if __name__ == "__main__":
    main()