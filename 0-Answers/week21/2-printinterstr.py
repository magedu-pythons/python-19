# 2、给出2个字符串，打印出所有由这2个字符串交替组成的字符串，要求维持原有字符的相对顺序。
# 例如：
#     输入"AB"和“CD”,输出：
#      ABCD、ACBD、ACDB、CABD、CADB、CDAB

def print_interval_strings(s1, s2, so_far):
    if len(s1) == 0 and len(s2) == 0:
        return
    if not s1:
        print(so_far+s2)
        return
    if not s2:
        print(so_far+s1)
        return
    print_interval_strings(s1[1:], s2, so_far+s1[0])
    print_interval_strings(s1, s2[1:], so_far+s2[0])

print_interval_strings('AB', 'CD', '')