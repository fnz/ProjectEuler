precedence = dict()

precedence['+'] = 2
precedence['-'] = 2
precedence['*'] = 3
precedence['/'] = 3
precedence['^'] = 4
precedence['('] = 0


def is_op(token):
    return token in precedence.keys()


def tokenize(sequence):
    ret = [s for s in sequence if s != ' ']
    return ret


def shunting_yard(tokens):
    ret = []
    stack = []
    for token in tokens:
        if token == '(':
            stack.append('(')
        elif token == ')':
            while stack[-1] != '(':
                ret.append(stack.pop())
            stack.pop()
        elif not is_op(token):
            ret.append(token)
        else:
            while stack and precedence[token] <= precedence[stack[-1]]:
                ret.append(stack.pop())
            stack.append(token)

    while stack:
        ret.append(stack.pop())

    return ret


def get_result(tokens):
    args = []
    for token in tokens:
        if not is_op(token):
            args.append(token)
        else:
            b = int(args.pop())
            a = int(args.pop())
            if token == '+':
                args.append(a + b)
            elif token == '-':
                args.append(a - b)
            elif token == '*':
                args.append(a * b)
            elif token == '/':
                args.append(a / b)
            elif token == '^':
                args.append(a ** b)

    return args.pop()


def main():
    tokens = tokenize('2^3 - (8 + ((1 + 1)^3))*2')
    tokens = shunting_yard(tokens)
    print get_result(tokens)

    # print get_result(list('238*+'))


if __name__ == '__main__':
    main()