def main():
    print max([sum(map(lambda x: int(x), list(str(i**j)))) for i in xrange(101) for j in xrange(101)])


if __name__ == '__main__':
    main()