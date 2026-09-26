para = "The tomb is definitely haunted haunted"
words = para.split()
print("No of words:", len(words))

uniqueness = dict()
for word in words:
    if word in uniqueness:
        uniqueness[word] += 1
    else:
        uniqueness[word] = 1

print(uniqueness)

# [the, tomb, is, haunted, the , tomb, tomb, the ,is , an]
# ---> set
# {the, tomb, is , haunted, an}