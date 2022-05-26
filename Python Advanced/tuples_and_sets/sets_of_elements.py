n, m = input().split()
n_set = set()
m_set = set()

for _ in range(int(n)):
    num = int(input())
    n_set.add(num)

for _ in range(int(m)):
    num = int(input())
    m_set.add(num)

intersection_set = n_set.intersection(m_set)

for num in intersection_set:
    print(num)

