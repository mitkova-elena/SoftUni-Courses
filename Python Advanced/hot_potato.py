from collections import deque

kids_input = input()
kids_queue = deque(kids_input.split())
toss = int(input())
counter = 0

while len(kids_queue) > 1:
    kid = kids_queue.popleft()
    counter += 1
    if counter < toss:
        kids_queue.append(kid)
    else:
        print(f"Removed {kid}")
        counter = 0

print(f"Last is {''.join(kids_queue)}")

