# 2、实现一个LRU缓存类，至少包含get和put方法

# LRU(Least Recently Used),最近最少使用缓存算法数据结构
# 使用一个list保存最近访问的元素，get、set对它进行key位置更新，并用字典进行查找元素

class LRUCache:
    def __init__(self, size):
        self.cache, self.size, self.recent = {}, size, []

    def get(self, key):
        if key not in self.recent:
            return -1
        else:
            self.update_recent(key)
            return self.cache[key]

    def set(self, key, value):
        self.cache[key] = value
        self.update_recent(key)

    def update_recent(self, key):
        if key in self.recent:
            self.recent.remove(key)
        elif len(self.cache) > self.size:
            del self.cache[self.recent[0]]
            self.recent = self.recent[1:]
        self.recent.append(key)





