# 1、实现3个线程交替打印 abcabcabc...，一个打印a，一个打印b，一个打印c
import threading
import logging

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


class PrintAlpha:
    def __init__(self, alpha='x'):
        self.alpha = alpha
        self.event = threading.Event()

    def print_alpha(self):
        while True:
            if self.event.is_set():
                print(self.alpha, end='')
                self.event.clear()


def main():
    p1 = PrintAlpha('a')
    p2 = PrintAlpha('b')
    p3 = PrintAlpha('c')

    t1 = threading.Thread(target=p1.print_alpha, name='p1')
    t2 = threading.Thread(target=p2.print_alpha, name='p2')
    t3 = threading.Thread(target=p3.print_alpha, name='p3')

    t1.start()
    t2.start()
    t3.start()

    while True:
        p1.event.set()
        threading.Event().wait(0.1)
        p2.event.set()
        threading.Event().wait(0.1)
        p3.event.set()
        threading.Event().wait(0.1)


if __name__ == '__main__':
    main()

# 2、输入一个字符串，求不含有重复字母的最长子串长度   
def lengthOfLongestSubstring(s):
    str_dict = {}
    one_max = 0
    start = 0
    for i in range(len(s)):
        if s[i] in str_dict and str_dict[s[i]] >= start:
            start = str_dict[s[i]] + 1
        one_max = i - start + 1
        str_dict[s[i]] = i
        max_len = max(max_len, one_max)
    return max_len

# test
print(lengthOfLongestSubstring('pwwssffasdf'))
