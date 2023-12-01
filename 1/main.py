import re

data = []
with open("test.txt") as file:
    data = file.readlines()

# Part 1
accum = 0
for line in data:
    for i in range(len(line)):
        if line[i] in "1234567890":
            accum += int(line[i]) * 10
            break
    for i in reversed(range(len(line))):
        if line[i] in "1234567890":
            accum += int(line[i])
            break

print(accum)

# Part 2
conversion = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eigth": "8",
    "nine": "9",
}
regex = f"[{''.join(conversion.keys())}]"
accum = 0

for line in data:
    match = re.search(regex, line)
    if match:
        line = line[match.start():].replace(match.group(),conversion.get(match.group()))
    match = re.search(regex, line)
    if match:
        line = line[match.start():].replace(match.group(),conversion.get(match.group()))
    print(line)
    for i in range(len(line)):
        if line[i] in "1234567890":
            accum += int(line[i]) * 10
            break
        if line[i] in "1234567890":
            accum += int(line[i]) * 10
            break
    for i in reversed(range(len(line))):
        if line[i] in "1234567890":
            accum += int(line[i])
            break

print(accum)