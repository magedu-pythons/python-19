# 1、题目描述：代码库的版本号是从 1 到 n 的整数。某一天，有人提交了错误版本的代码，
# 因此造成自身及之后版本的代码在单元测试中均出错。请找出第一个错误的版本号。
# 你可以通过 isBadVersion 的接口来判断版本号 version 是否在单元测试中出错，
# 具体接口详情和调用方法请见代码的注释部分。
# 例如：
# 给出 n=5
# 调用isBadVersion(3)，得到false
# 调用isBadVersion(5)，得到true
# 调用isBadVersion(4)，得到true
# 此时我们可以断定4是第一个错误的版本号

def isBadVersion(version):
    pass


def find_first_bad_version(n):
    # 2分查找
    start, end = 1, n
    while start + 1 < end:
        mid = (start + end) / 2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid
    if isBadVersion(start):
        return start
    return end
