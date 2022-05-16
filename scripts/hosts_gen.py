import os
import subprocess

from agg import calc

def gen(n, F):
    f = open("/Users/mukkhakimov/Documents/itmo/thesis/hosts.txt", 'w')
    f.write(str(F) + '\n')
    f.write("http://localhost:8080" + '\n')
    for i in range(n - 1):
        f.write("http://localhost:" + str(i + 9000) + ('\n' if i != n - 2 else ''))
    f.close()

os.system("cd /Users/mukkhakimov/GolandProjects/broadcasts-instance/cmd && go build github.com/mrhakimov/broadcasts-single-instance/cmd")
os.system("cd /Users/mukkhakimov/GolandProjects/broadcasts/cmd && go build github.com/mrhakimov/broadcasts-source/cmd")
os.system("cd /Users/mukkhakimov/GolandProjects/broadcasts-benchmarks/cmd && go build github.com/mrhakimov/broadcasts-benchmarks/cmd")

for mbytes in [1000000]:
    for n in range(4, 12):
        for f in range(0, (n - 1) // 5 + 1):
            gen(n, f)

            file = open("/Users/mukkhakimov/Documents/itmo/thesis/logs.txt", 'w')
            file.close()

            insts = subprocess.Popen(f"/Users/mukkhakimov/GolandProjects/broadcasts-instance/cmd/cmd -n={n} -f={f}".split())
            source = subprocess.Popen(f"/Users/mukkhakimov/GolandProjects/broadcasts/cmd/cmd -n={n} -f={f}".split())

            print(insts.pid)
            print(source.pid)
            
            # os.system(f"cd /Users/mukkhakimov/GolandProjects/broadcasts-instance/cmd && ./cmd -n={n} -f={f}")
            # os.system(f"cd /Users/mukkhakimov/GolandProjects/broadcasts/cmd && ./cmd -n={n} -f={f}")
            bench = subprocess.Popen(f"/Users/mukkhakimov/GolandProjects/broadcasts-benchmarks/cmd/cmd -mbytes={mbytes} -broadcast=cebrb".split())
            print(bench.pid)
            bench.wait()

            avg, mn, mx = calc()

            os.system(f"kill {insts.pid}")
            os.system(f"kill {source.pid}")
            # os.system(f"kill {bench.pid}")

            results = open("/Users/mukkhakimov/Documents/itmo/thesis/results_cebrb.txt", 'a')
            results.write(f'n = {n}, f = {f}\n')
            results.write(f'avg = {avg}, min = {mn}, max = {mx}\n')
            results.close()

        for f in range(0, (n - 1) // 3 + 1):
            gen(n, f)

            file = open("/Users/mukkhakimov/Documents/itmo/thesis/logs.txt", 'w')
            file.close()

            insts = subprocess.Popen(f"/Users/mukkhakimov/GolandProjects/broadcasts-instance/cmd/cmd -n={n} -f={f}".split())
            source = subprocess.Popen(f"/Users/mukkhakimov/GolandProjects/broadcasts/cmd/cmd -n={n} -f={f}".split())

            print(insts.pid)
            print(source.pid)
            
            # os.system(f"cd /Users/mukkhakimov/GolandProjects/broadcasts-instance/cmd && ./cmd -n={n} -f={f}")
            # os.system(f"cd /Users/mukkhakimov/GolandProjects/broadcasts/cmd && ./cmd -n={n} -f={f}")
            bench = subprocess.Popen(f"/Users/mukkhakimov/GolandProjects/broadcasts-benchmarks/cmd/cmd -mbytes={mbytes} -broadcast=brb".split())
            print(bench.pid)
            bench.wait()

            avg, mn, mx = calc()

            os.system(f"kill {insts.pid}")
            os.system(f"kill {source.pid}")
            # os.system(f"kill {bench.pid}")

            results = open("/Users/mukkhakimov/Documents/itmo/thesis/results_brb.txt", 'a')
            results.write(f'n = {n}, f = {f}\n')
            results.write(f'avg = {avg}, min = {mn}, max = {mx}\n')
            results.close()
