import sys

def replace_digits(s):
    count = sum(1 for ch in s if ch.isdigit())  # 统计数字个数
    s = list(s)
    s.extend([''] * (count * 5))  # 扩展列表长度，以容纳 "number"
    print(len(s))

    s_old_index = len(s) - count * 5 - 1  # 旧索引（原始字符串末尾）
    s_new_index = len(s) - 1  # 新索引（扩展后的字符串末尾）

    # 指针顺着旧字符串，从后往前 遍历替换数字。比如a1b2c，从c开始向a遍历。
    while s_old_index >= 0:
        if s[s_old_index].isdigit():  # 如果是数字，替换成 "number"
            for ch in "number"[::-1]:  # 逆序填充 "number"
                s[s_new_index] = ch
                s_new_index -= 1
        else:
            s[s_new_index] = s[s_old_index]  # 复制原字符
            s_new_index -= 1
        s_old_index -= 1

    return ''.join(s)  # 重新转换为字符串


# 读取输入
for line in sys.stdin:
    print(replace_digits(line.strip()))
