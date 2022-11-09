n = int(input())
all_usernames = set()

for _ in range(n):
    username = input()
    all_usernames.add(username)

print("\n".join(all_usernames))

