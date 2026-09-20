def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = 236
if is_even(num):
    print("It is even")
else:
    print("It is odd")