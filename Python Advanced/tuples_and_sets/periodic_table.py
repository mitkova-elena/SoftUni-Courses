n = int(input())
chemical_elements = set()

for _ in range(n):
    current_elements = set(input().split())
    chemical_elements = chemical_elements.union(current_elements)

for element in chemical_elements:
    print(element)

