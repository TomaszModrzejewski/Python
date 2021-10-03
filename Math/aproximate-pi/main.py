def approxPi(num): 
    prev = 1
    current = 0
    i = 1
    sign = 1
    while abs(current - prev) > num:
        prev = current
        current += sign * (4/i)
        i += 2
        sign = -sign
        #print(current)
    return current

print(approxPi(0.01))      # 3.1465677471829556 
print(approxPi(0.0000001)) # 3.1415927035898146
