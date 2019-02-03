import random
for i in range(1, 201):
    num_range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    string_range = ['a', 'b', 'c', 'd', 'e', 'r', 't', 'y', 'u',
                    'i', 'o', 'p', 's', 'f', 'g', 'h'
                    'j', 'k', 'l', 'z', 'x', 'v', 'b', 'n', 'm']

    index_string = random.randint(0, 23)
    index_num = random.randint(0, 9)
    string_len = random.randint(6, 8)
    string_p = ""
    for j in range(0, string_len):
        if random.randint(1, 2) == 1:
            if random.randint(1, 2) == 1:
                string_p += string_range[index_string]
            else:
                string_p += string_range[index_string].upper()
        else:
            string_p += str(num_range[index_num])
    print(string_p)


# test
#运行上述的代码可以得到：
#200 个随机生成的优惠券码
# ll44L4l4
# 9S999S9
# 88Bbb8bb
# 8SssSsS
# 000O0OO
 #>>>>



