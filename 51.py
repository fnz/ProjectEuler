from primes import *
from collections import Counter


def get_groups(n):
    ret = {}
    s = str(n)
    c = Counter(s)
    for k, v in c.iteritems():
        if v > 1:
            pos = [i for i in range(len(s)) if s[i] == k]
            ret[k] = pos

    return ret


def get_family_size(n, pos):
    ret = 0
    s = list(str(n))
    for i in range(10):
        for p in pos:
            s[p] = str(i)

        ss = ''.join(s)
        if ss[0] != '0' and is_prime(int(ss)):
            ret += 1

    return ret


def main():
    for n in gen_primes():
        for m, pos in get_groups(n).iteritems():
            if get_family_size(n, pos) == 8:
                print n
                return


if __name__ == '__main__':
    main()