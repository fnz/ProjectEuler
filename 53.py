from combinatorics import *


def main():
    ret = 0
    for i in range(101):
        for j in range(i + 1):
            if nCr(i, j) > 1000000:
                ret += i + 1 - 2*j
                break

    print ret

if __name__ == "__main__":
    main()


