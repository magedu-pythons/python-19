#1.#"1,2,3" 变成 ["1","2","3"]

print(str("1,2,3".split(",")).replace("'",'"'))

#2.


#3.li=[[]] * 5 生成[[],[],[],[],[]],列表0-4的元素都指向同一个物理地址。0-4的元素
# 变化就是对着一个物理地址的修改，会影响其他元素都会变化。在列表的最后追加元素，
# 并没有对前5个元素有任何改写，所以前四个元素没有变化