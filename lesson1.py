# Task 1
total_time = int(input('Введите кол-во секунд: '))
intervals = {'days': 86400, 'hours': 3600, 'minutes': 60, 'seconds': 1}
to_print = ''
for interval in intervals:
    int_val = total_time // intervals[interval]
    total_time = total_time - (int_val * intervals[interval])
    if int_val > 0:
        to_print += interval + ' ' + str(int_val) + ' '
print(to_print)

# Task 3
idx = 0
word = 'процент'
end_word = ''
while idx <= 100:
    val = idx - ((idx // 10) * 10)
    if (val == 0) or (val > 4 and val <= 9) or (idx > 10 and idx < 15):
        end_word = 'ов'
    elif val > 1 & val < 5:
        end_word = 'а'
    else:
        end_word = ''
    print(str(idx) + ' ' + word + end_word + ' ')
    idx += 1



