def findPrime(p):
    count = 1
    prime = 1
    while count <= p: # while counting to the number we need
        for n in range(1,p+1): #
            if count%n != 0:
                prime = count
                print "!!!!"
                count += 1
                print count
            else:
                print "fuuuuck"
                count +=1
    return prime

def findPrime2(n):
    count = 3
    prime = [2]
    count2 = 1
    while count <= n:
        while count2 <= 100:
            for r in range(2,100):
                if r%!=0:
                    prime.append(r)
                    print "YAY!!", count, count2, prime
                    count2 += 1
                    count += 1
                else:
                    print "fuuuck"
                    count2 += 1
            count += 1

    return prime

print findPrime2(6)
