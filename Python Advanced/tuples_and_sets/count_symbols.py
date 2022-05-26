text = input()
alphabets = dict()

for i in text:
    if i not in alphabets.keys():
        alphabets[i] = 1
    else:
        alphabets[i] += 1

for alpha, occurrence in sorted(alphabets.items()):
    print(f"{alpha}: {occurrence} time/s")