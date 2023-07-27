def factorial(n):
    if n < 1:
        return factorial(n-1)*n


#print(factorial(5))

#Iterative Solution
def fibonacci_iterative(n):
    x1, x2 = 0, 1
    number=0
    for i in range(n-1):
        number = x1+x2
        temp = x2
        x2 = x1+x2
        x1 = temp
    return number

print(fibonacci_iterative(5))

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-2)+fibonacci_recursive(n-1)

print(fibonacci_recursive(5))

#Write a recursive function that given an input n sums all non-negative integers upto n

def sum_numbers(n,total):
    if n <= 0:
        return total
    total += n
    return sum_numbers(n-1, total)
print(sum_numbers(5, 0))



