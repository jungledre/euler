def prim(n):
    count = 1
    new = n
    while count < new:
        if new%count == 0:
            print count
            new = n/count
            count += 1
        else:
            count += 1

print prim(600851475143)
#use second to last number...
# answer 6857
