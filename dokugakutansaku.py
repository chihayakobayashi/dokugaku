def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

numbers = range(1,100)

s1 = ss(numbers,10)
print(s1)

