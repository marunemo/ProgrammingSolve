t = int(input())
roomNumber = []
for _ in range(t):
    h, w, n = map(int, input().split())
    # -1 for indexing
    n -= 1
    # +1 for regarding start from 1, not 0
    roomNumber.append((n % h + 1) * 100 + (n // h + 1))
print(*roomNumber, sep='\n')