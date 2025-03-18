# Write a program that takes two integers, N and M (N ≤ M), as input and calculates the sum of
#  cubes of all numbers in the range [N, M]


import sys 

def cube_sum(n,m):
    if n > m :
        return -1
    sum = 0
    for i in range(n,m+1):
        sum = sum + i**3
        
    return sum



#  Write a program that takes two integers, N and M (N ≤ M), as input and finds the sum of all
#  prime numbers in the range [N, M]
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def prime_sum(n,m):
    if n > m:
        return -1
    sum =0
    for i in range(n,m+1):
        if is_prime(i):
            sum = sum + i
    return sum

def is_perfect(n):
    if n < 1:
        return False
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def is_harshad(n):
    if n == 0:
        return False
    sum_of_digits = sum(int(digit) for digit in str(n))
    return n % sum_of_digits == 0

def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
    return sum_of_powers == n

def main():
    data = sys.stdin.readline().split()
    n = int(data[0])
    m = int(data[1])
    results = cube_sum(n,m)
    print("Sum of cubes of Numbers ranging from N to M",results)
    prime_results = prime_sum(n,m)
    print("Sum of prime numbers ranging from N to M",prime_results)
    
    perfect_numbers = [i for i in range(n, m+1) if is_perfect(i)]
    print("Perfect numbers in the range [N, M]:", perfect_numbers)
    
    harshad_numbers = [i for i in range(n, m+1) if is_harshad(i)]
    print("Harshad numbers in the range [N, M]:", harshad_numbers)
    
    armstrong_numbers = [i for i in range(n, m+1) if is_armstrong(i)]
    print("Armstrong numbers in the range [N, M]:", armstrong_numbers)

if __name__=="__main__":
    main()