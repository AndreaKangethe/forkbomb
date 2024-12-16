from multiprocessing import process, cpu_count, Process
import time

def fork():
    p = Process(target=fork)
    p.start()
    p.join()
    return p

def count(number):
    while number > 0:
        number -= 1
        time.sleep(1)


def spawn(nump):
    process = [Process(target=count, args=(1000,)) for i in range(nump)]
    for p in process:
        p.start()
        print(f'Started process {p.pid}.')

    for p in process:
        p.join()
        print(f'Finished process {p.pid}.')

def main():
    nump = cpu_count()
    nump = nump * 200
    print(f'Number of processes: {nump}')
    print(f'Spawning {nump} processes')
    print(f'Warning !! This process will take a while')
    spawn(nump)

if __name__ == '__main__':
    main()