def isPal(min = 100, max = 999):
    max_pal = 0
    a = 999
    while a > 99:
        b = 999
        while b >= a:
            prod = a*b
            if prod > max_pal and str(prod) == str(prod)[::-1]:
                max_pal = prod
            b -= 1
        a -= 1
    return max_pal

print isPal()

#906609
