def is_palindrome(string):
    for i in range(0, len(string) / 2):
        if string[i] != string[-i - 1]:
            return False

    return True


def is_lychrell(x):
    for i in range(50):
        x += int(str(x)[::-1])
        if is_palindrome(str(x)):
            return False

    return True


def main():
    ret = 0
    for x in range(10000):
        if is_lychrell(x):
            ret += 1

    print ret


if __name__ == '__main__':
    main()
