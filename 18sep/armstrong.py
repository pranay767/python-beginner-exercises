def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    # n = 45 --> digits = "45" --> power = len("45") = 2
    # If 4^2 + 5^2 = 45, then 45 is armstrong number
    return sum(int(d) ** power for d in digits) == n

def armstrong_nums_in_range(start, end): # function has to give
    armstrong_numbers_start_end = []
    for i in range(start,end+1):
        if is_armstrong(i):
            armstrong_numbers_start_end.append(i)
    return armstrong_numbers_start_end

def count_armstrong_numbers(start, end):
    count = 0

    for i in range(start, end + 1):
        if is_armstrong(i):
            count += 1

    return count

num = 153
if is_armstrong(num):
    print(num, "is armstrong number")
else:
    print(num ,"is not armstrong number")

print(armstrong_nums_in_range(0,200))
print(count_armstrong_numbers(0, 200))

# digits = "45"
# for d in digits:
#     print(type(d))