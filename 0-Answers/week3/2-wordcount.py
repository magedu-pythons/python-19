
#2、任一个英文的纯文本文件，统计其中的单词出现的个数
import re
def words_count(file_text):
    count_dict = {}
    with open(file_text, 'r') as f:
        for line in f:
            ignore_list = re.findall(r'[^a-zA-Z]+', line)
            # [',', '! ']
            for ignore in ignore_list:
                line = line.replace(ignore, ' ')
            lines = line.split(' ')
            # abc def hello
            # ['abc', 'def', 'hello']

            for word in lines:
                if word.isalpha():
                    if word not in count_dict:
                        count_dict[word] = 1
                    else:
                        count_dict[word] += 1
    return count_dict