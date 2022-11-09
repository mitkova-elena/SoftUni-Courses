n = int(input())
odd_set = set()
even_set = set()

for i in range(1, n+1):
    name = input()
    ascii_value_of_the_name = 0
    for ch in name:
        value = ord(ch)
        ascii_value_of_the_name += value
    ascii_value_of_the_name //= int(i)
    if ascii_value_of_the_name % 2 == 0:
        even_set.add(ascii_value_of_the_name)
    else:
        odd_set.add(ascii_value_of_the_name)

even_sum = sum(even_set)
odd_sum = sum(odd_set)

if even_sum == odd_sum:
    result = odd_set.union(even_set)
elif even_sum <= odd_sum:
    result = odd_set.difference(even_set)
elif even_sum >= odd_sum:
    result = odd_set.symmetric_difference(even_set)

print(*result, sep=', ')

