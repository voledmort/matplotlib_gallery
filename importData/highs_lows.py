from datetime import datetime

from matplotlib import pyplot as plt
import csv

filename = 'D:\Working\PycharmProjects\matplotlib_gallery\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    dates, highs = [],[]
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

    print(highs)

    # for index, column_header in enumerate(header_row):
        # print(index, column_header)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature", fontsize=16)
    plt.tick_params(which='major', labelsize=16)
    plt.show()