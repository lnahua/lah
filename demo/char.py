
'''
#1456定长子串中元音的最大数目
给你字符串 s 和整数 k 。

请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。

英文中的 元音字母 为（a, e, i, o, u）
'''
s = "abciiidef"
k = 3
n = len(s)
if k >= n:
    print('0')
count = 0
for i in range(k):
    if s[i] in ['a','i','o','u','e']:
        count += 1
j = k
max_value = count
while j < n:
    if s[j] in ['a','i','o','u','e']:
        count += 1
    if s[j-k] in ['a','i','o','u','e']:
        count -= 1
    j += 1
    max_value = max(max_value,count)

print(max_value)
