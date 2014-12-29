def smallestMult():
    count = 1
    s = 1
    while count <= 10000000000:
        for n in range(1,21):
            if count%n == 0:
                s = count
                print s
            else:
                count += 1
    return s

print smallestMult()

# ! INCOMPLETE

# Answer: 232792560
# Errors out at correct answer..
