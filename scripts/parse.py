from collections import defaultdict
import matplotlib.pyplot as plt


def parse(path):
    f = open(path)
    data = f.read().split('\n')
    f.close()

    mp = defaultdict(dict)

    mbytes = 1
    i = 0
    for line in data:
        if line == '':
            mbytes *= 100
            i += 1
            continue

        parts = line.split(', ')
        n, f, avg, mn, mx = map(lambda x: float(x.split(' = ')[1]), parts)
        n, f = int(n), int(f)

        if mp[i].get(f) is None:
            mp[i][f] = []

        mp[i][f].append((n, avg))

    for i in range(4):
        for f in range(3):
            print(mp[i][f])

    return mp


mp1 = parse("/Users/mukkhakimov/Documents/itmo/thesis/results_2.txt")
mp2 = parse("/Users/mukkhakimov/Documents/itmo/thesis/results_3.txt")

for i, mbytes in enumerate([1, 100, 10000, 1000000]):
    # if mbytes != 1000000:
    #     continue
    for f in range(3):
        x1, y1 = [], []
        x2, y2 = [], []

        for p in mp1[i][f]:
            x1.append(p[0])
            y1.append(p[1])

        for p in mp2[i][f]:
            x2.append(p[0])
            y2.append(p[1])

        print(y1, y2)

        ln = len(x2)
        x1 = x1[len(x1) - ln:]
        y1 = y1[len(y1) - ln:]

        # if f == 0:
        p1, p2 = plt.plot(x1, y1, 'r', x2, y2, 'b')
        plt.legend([p1, p2], ['BRB', 'CEBRB'])
        print(y2)
        # else:
        #     x3, y3 = [], []
        #     for p in mp1[i][2]:
        #         x3.append(p[0])
        #         y3.append(p[1])
        #
        #     print(x1, x2, x3)
        #     plt.plot(x1, y1, 'r', x2, y2, 'b', x3, y3, 'g')
        plt.xlabel('N')
        plt.ylabel('latency (ms)')
        plt.suptitle(f'mbytes = {mbytes}, f = {f}')
        plt.show()
