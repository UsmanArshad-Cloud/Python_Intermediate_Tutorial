#Iterative Way to compute Power:
def Power(base,exponent):
    result = 1
    for i in range(exponent):
        result = (result*base)
    return result

print(Power(2,3))

#Recursive Way

#n time complexity
def power(base,exp):
    if exp == 0:
        return 1
    return (base*power(base, exp-1))

print(power(2,3))

#log n complexity

def Power_N(base,exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        if(exponent%2 == 0):
            return Power_N(base, exponent//2)*Power_N(base, exponent//2)
        else:
            return base*Power_N(base,exponent-1)


print(Power_N(2,3))