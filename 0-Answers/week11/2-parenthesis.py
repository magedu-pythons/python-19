# 2、打印出N对合理的括号组合。
# 例如： 当N=3，输出：()()(),()(()),(())(),((())),(()())


def print_parenthesis(output, opend, close, pairs):
    """
    左右括号数量匹配
    :param output:
    :param opend:
    :param close:
    :param pairs:
    :return:
    """
    if opend == pairs and close == pairs:
        print(output)
    else:
        if opend < pairs:
            print_parenthesis(output + '(', opend + 1, close, pairs)
        if close < opend:
            print_parenthesis(output + ')', opend, close + 1, pairs)


print_parenthesis('', 0, 0, 3)
