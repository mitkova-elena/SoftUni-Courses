n = int(input())
longest_length = 0
longest_set = list()

for _ in range(n):
    first_set = set()
    second_set = set()

    first_range, second_range = (input().split("-"))

    first_start, first_end = [int(x) for x in first_range.split(",")]
    second_start, second_end = [int(x) for x in second_range.split(",")]

    for i in range(first_start, first_end + 1):
        first_set.add(i)
    for j in range(second_start, second_end + 1):
        second_set.add(j)
    intersection_set = first_set.intersection(second_set)
    if len(intersection_set) > longest_length:
        longest_length = len(intersection_set)
        longest_set = list(intersection_set)

print(f"Longest intersection is {longest_set} with length {longest_length}")
