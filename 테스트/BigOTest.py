import time

def timeTaken(iter, n):
    start = time.perf_counter()
    check = n in iter
    end = time.perf_counter()
    return end - start

l = list()
s = set()
d = dict()

for i in range(0, 1000000):
    l.append(i)
    s.add(i)
    d[i] = True

# Check best case of each
print("======", "Best", "======")
print("list : %.10f" % timeTaken(l, 0))
print("set : %.10f" % timeTaken(s, 0))
print("dict : %.10f" % timeTaken(d, 0))

# Check worst case of each
print("======", "Worst", "======")
print("list : %.10f" % timeTaken(l, 999999))
print("set : %.10f" % timeTaken(s, 999999))
print("dict : %.10f" % timeTaken(d, 999999))

# Check average case of each
print("======", "Average", "======")
print("list : %.10f" % timeTaken(l, 55555))
print("set : %.10f" % timeTaken(s, 55555))
print("dict : %.10f" % timeTaken(d, 55555))