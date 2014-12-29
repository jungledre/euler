count = 1
sum = 0

while count < 1000:
    if count%3 == 0 or count%5 == 0:
        sum += count
        count += 1
    else:
        count += 1

print sum

#answer 233168
