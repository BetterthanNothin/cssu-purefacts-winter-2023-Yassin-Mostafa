import numpy as np

def time_to_number(date: str) -> int:
    i = date.split(":")
    return int(i[0])*60 + int(i[1])


def number_to_time(num: int) -> str:
    return str(num//60) + ":" + str(num % 60)


def load_file(file):
    useless, start_times, end_times = np.loadtxt(file, dtype=str, delimiter=",", unpack=True)
    return [start_times[1:], end_times[1:]]


def do(file_name) -> str:
    x = load_file(file_name)
    pairs = []
    total = []
    for i in range(len(x[0])):
        pairs.append([time_to_number(x[0][i]), time_to_number(x[1][i])])
        total.extend([time_to_number(x[0][i]), time_to_number(x[1][i])])
    total.sort()
    rang = 0
    start = 0
    for t in range(len(total) - 1):
        st = total[t]
        et = total[t + 1]
        good = True
        for i in pairs:
            if st in range(i[0], i[1]) and et in range(i[0], i[1]):
                good = False

        if good and (et - st) > rang:
            rang = et - st
            start = st

    if rang == 0:
        return "None"
    return "Start Time: " + number_to_time(start) + ", Range: " + str(rang)


if __name__ == "__main__":
    print(do("test1.csv"))
    print(do("test2.csv"))
    print(do("test3.csv"))
    print(do("test4.csv"))
    print(do("test5.csv"))




