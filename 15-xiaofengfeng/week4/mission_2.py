import re
import pprint
from collections import Counter


with open('story.txt') as f:
    origin_text = f.read()
wordpat = re.compile(r"([a-zA-Z]+([-|'][a-zA-Z]+)?)")
wordlist = [item[0].lower() for item in wordpat.findall(origin_text)]
wordcount = Counter(wordlist)
result = [(k, v) for k, v in wordcount.items()]
result.sort(key=lambda x: x[1], reverse=True)
pprint.pprint(result)