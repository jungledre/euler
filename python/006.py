def findDiff():
    sumsq = 0
    sqs = 0
    count = 1
    diff = 0
    while count <= 100:
        sumsq += count**2
        sqs += count
        count += 1
    sqs = sqs**2
    diff = sqs - sumsq
    return diff

print findDiff()

# Answer: 25164150
