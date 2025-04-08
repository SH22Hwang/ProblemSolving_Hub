def main():
    n = int(input())
    size = list(map(int, input().split()))
    t, p = map(int, input().split())

    # s, m, ... 몫을 구한 다음 다 더하면 될 듯
    num_shirts = 0
    for i in size:
        shirts = i // t
        num_shirts += shirts
        if i % t:
            num_shirts += 1

    num_pen_sets = n // p
    num_pens = n % p

    print(f'{num_shirts}\n{num_pen_sets} {num_pens}')


if __name__ == "__main__":
    main()