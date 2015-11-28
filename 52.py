def main():
    x = 0
    while True:
        x += 1

        l = {}
        n = 6

        for i in range(n):
            l[i] = sorted(list(str((i + 1) * x)))

        t = True
        for i in range(n):
            if l[i] != l[(i + 1) % n]:
                t = False
                break

        if not t:
            continue

        print x
        return


if __name__ == '__main__':
    main()