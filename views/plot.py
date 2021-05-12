import matplotlib.pyplot as plt
import csv
def plotGraph():
    x = []
    y = []

    with open('xl2.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[1]))
            y.append(int(row[0]))

    plt.plot(x, y)
    plt.xlabel('Time(ms)')
    plt.ylabel('Y')
    plt.title('ECG')
    plt.show()
