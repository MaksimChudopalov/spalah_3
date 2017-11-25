import time


def foo(n):
    for i in range(n):
        pass

start_time = time.time()
foo(100000)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
foo(10000000)
print("--- %s seconds ---" % (time.time() - start_time))