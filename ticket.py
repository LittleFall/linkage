import math

# 1. Basel Problem
ans = 0
for i in range(1, 10000):
    ans += 1 / (i * i)
print(ans)  # 1.6448340618480652
print(math.pi * math.pi / 6)  # 1.6449340668482264

# 2. sqrt(1+2*sqrt(1+3*sqrt(1+4*sqrt(1+...))))
ans = 1
for i in range(10000, 0, -1):
    ans = i * math.sqrt(1+ans)
print(ans)  # 3.0
