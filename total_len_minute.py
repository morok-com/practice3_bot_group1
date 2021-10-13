def calc_stat(listened):  # от англ. calculate statistics, посчитать статистику
    # напишите код функции calc_stat
    total_len_minute = 0
    for len_minute in range(len(listened)):
        total_len_minute += listened[len_minute]
    return f'Вы прослушали {len(listened)} песен, общей продолжительностью {total_len_minute // 60} минут'

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))