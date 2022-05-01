def sum_digits(str):
    sum = 0
    for i in str:
        if i.isdigit() == True:
            sum += int(i)
    return sum
s = input()
print(sum_digits(s))