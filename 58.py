def main():
    ret = 0
    n, m = 1, 2

    for i in xrange(1000):
        if len(str(3*m + n)) > len(str(2*m + n)):
            ret += 1

        n, m = m, 2*m + n

    print ret

if __name__ == '__main__':
    main()
