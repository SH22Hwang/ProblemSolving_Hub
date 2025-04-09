import math

def main():

    n, k = map(int, input().split())
    fac = math.factorial
    print( int(fac(n) / (fac(k) * fac(n-k))) )

if __name__ == "__main__":
    main()