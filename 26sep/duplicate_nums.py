duplicates_status = {}
duplicates = set()
#dictoinary is the best way to do this, the best data struvture
while True:
    num = input()
    if num=='0':
        break
    if num in duplicates_status:
        duplicates_status[num] += 1
    else:
        duplicates_status[num] = 1

print(duplicates_status)

for key, value in duplicates_status.items():
    if value > 1:
        duplicates.add(key)

print(len(duplicates), "duplicates")