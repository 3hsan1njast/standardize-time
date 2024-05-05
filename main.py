def standardize_time(seconds: int):
    time = [0, 0]
    # time[0] -> Minutes
    # time[1] -> Seconds
    time[0] = str((seconds / 60).__floor__())
    time[1] = str(seconds % 60)
    # ↓ Adding "0" before the "second" if it had 1 digit ↓
    if time[1].__len__() == 1:
        time[1] = f'0{time[1]}'

    return f'{time[0]}:{time[1]}'
