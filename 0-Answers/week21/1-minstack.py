# 1、实现一个带能获取最小值get_min方法的栈，get_min方法将返回当前栈中的最小值。
# 实现的栈将支持push，pop 和 get_min 操作，所有操作要求都在O(1)时间内完成。


class MinStack:
    # 使用2个stack，一个min_stack每次存储最小的值
    #
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def get_min(self):
        if len(self.min_stack) == 0:
            return None
        else:
            return self.min_stack[-1]
