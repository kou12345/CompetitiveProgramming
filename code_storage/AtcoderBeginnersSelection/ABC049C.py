# ABC049C - 白昼夢

# dreameraser という文字列の場合、dreamer とも読み取れてしまうのでerase eraserから検証していく
word_list =  ['eraser', 'erase', 'dreamer', 'dream']

s = input()

# word_listと一致したものは消していく、sが空になればYES, そうでなければNO

for i in range(len(word_list)):
    s = s.replace(word_list[i], '')

if s == '':
    print('YES')
else:
    print('NO')
